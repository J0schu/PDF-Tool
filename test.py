import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsPixmapItem,
    QFileDialog,
)
from PySide6.QtCore import Qt, QSize, QRectF
from PySide6.QtGui import QPixmap
from PySide6.QtPdf import QPdfDocument

# Thumbnail constants
BASE_CELL_W = 200
BASE_CELL_H = 260
SPACING = 10


class DraggableGridItem(QGraphicsPixmapItem):
    def __init__(self, pixmap, row, col):
        super().__init__(pixmap)
        self.setFlags(
            QGraphicsPixmapItem.ItemIsMovable | QGraphicsPixmapItem.ItemIsSelectable
        )
        self.grid_row = row
        self.grid_col = col

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)

        # Calculate nearest grid cell
        target_col = round(self.x() / (BASE_CELL_W + SPACING))
        target_row = round(self.y() / (BASE_CELL_H + SPACING))

        # Clamp within valid range
        target_col = max(0, min(target_col, self.scene().grid_cols - 1))
        target_row = max(0, min(target_row, self.scene().grid_rows - 1))

        scene = self.scene()
        found = None

        # Find any item occupying target cell
        for item in scene.items():
            if isinstance(item, DraggableGridItem) and item is not self:
                if item.grid_row == target_row and item.grid_col == target_col:
                    found = item
                    break

        if found:
            orig_row, orig_col = self.grid_row, self.grid_col
            # Swap positions
            self.setPos(
                found.grid_col * (BASE_CELL_W + SPACING),
                found.grid_row * (BASE_CELL_H + SPACING),
            )
            found.setPos(
                orig_col * (BASE_CELL_W + SPACING), orig_row * (BASE_CELL_H + SPACING)
            )
            found.grid_row, found.grid_col = orig_row, orig_col
            self.grid_row, self.grid_col = target_row, target_col
        else:
            # Snap into empty cell
            self.setPos(
                target_col * (BASE_CELL_W + SPACING),
                target_row * (BASE_CELL_H + SPACING),
            )
            self.grid_row, self.grid_col = target_row, target_col


class PDFArrangerNoExpand(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Arranger (Fixed Scene)")
        self.resize(900, 600)

        self.layout = QVBoxLayout(self)
        self.load_btn = QPushButton("Load PDF")
        self.load_btn.clicked.connect(self.load_pdf)
        self.layout.addWidget(self.load_btn)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.layout.addWidget(self.view)

        self.items = []

    def load_pdf(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open PDF", "", "PDF Files (*.pdf)"
        )
        if not file_name:
            return

        doc = QPdfDocument(self)
        doc.load(file_name)

        self.scene.clear()
        self.items.clear()

        # Render pages
        for i in range(doc.pageCount()):
            size = QSize(BASE_CELL_W, BASE_CELL_H)
            img = doc.render(i, size)
            if img.isNull():
                continue
            pix = QPixmap.fromImage(img)

            item = DraggableGridItem(pix, 0, 0)
            self.items.append(item)
            self.scene.addItem(item)

        self.relayout()

    def relayout(self):
        width = self.view.viewport().width()
        cols = max(1, width // (BASE_CELL_W + SPACING))
        rows = (len(self.items) + cols - 1) // cols

        # Set a fixed scene rectangle based on columns/rows
        scene_width = cols * (BASE_CELL_W + SPACING)
        scene_height = rows * (BASE_CELL_H + SPACING)
        self.scene.setSceneRect(QRectF(0, 0, scene_width, scene_height))
        self.scene.grid_cols = cols
        self.scene.grid_rows = rows

        # Place items in grid positions
        for idx, item in enumerate(self.items):
            row = idx // cols
            col = idx % cols
            item.grid_row = row
            item.grid_col = col

            x = col * (BASE_CELL_W + SPACING)
            y = row * (BASE_CELL_H + SPACING)
            item.setPos(x, y)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.relayout()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFArrangerNoExpand()
    window.show()
    sys.exit(app.exec())
