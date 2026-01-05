import fitz
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QScrollArea, QVBoxLayout, QWidget


class PdfPreview(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._doc: fitz.Document | None = None
        self._pages: list[int] | None = None  # None = all pages
        self._zoom = 1.5
        self._fit_to_width = True

        # ---------------- Layout ----------------
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Scroll area
        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)
        layout.addWidget(self._scroll)

        # Container
        self._container = QWidget()
        self._container_layout = QVBoxLayout(self._container)
        self._container_layout.setAlignment(Qt.AlignTop)
        self._scroll.setWidget(self._container)

        # Resize debounce
        self._resize_timer = QTimer(self)
        self._resize_timer.setSingleShot(True)
        self._resize_timer.timeout.connect(self._render)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def load_pdf(self, path: str, pages: list[int] | None = None):
        self.clear()
        self._doc = fitz.open(path)
        self._pages = pages
        self._render()

    def set_pages(self, pages: list[int] | None):
        self._pages = pages
        self._render()

    def set_zoom(self, zoom: float):
        self._fit_to_width = False
        self._zoom = zoom
        self._render()

    def set_fit_to_width(self, enabled: bool = True):
        self._fit_to_width = enabled
        self._render()

    def clear(self):
        self._clear_widgets()
        self._pages = None

        if self._doc:
            self._doc.close()
            self._doc = None

    # ------------------------------------------------------------------
    # Qt Events
    # ------------------------------------------------------------------

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self._fit_to_width and self._doc:
            # debounce
            self._resize_timer.start(150)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _clear_widgets(self):
        while self._container_layout.count():
            item = self._container_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def _compute_fit_zoom(self, page):
        viewport_width = self._scroll.viewport().width() - 20
        if viewport_width <= 0:
            return 1.0
        return viewport_width / page.rect.width

    def _render(self):
        if not self._doc:
            return

        self._clear_widgets()

        pages = (
            self._pages
            if self._pages is not None
            else list(range(self._doc.page_count))
        )

        total_pages = len(pages)
        if total_pages == 0:
            return

        for visible_index, page_index in enumerate(pages, start=1):
            if page_index < 0 or page_index >= self._doc.page_count:
                continue

            # ---- Header Label ----
            header = QLabel(f"Page {page_index + 1}")
            header.setAlignment(Qt.AlignCenter)
            header.setStyleSheet(
                "background-color: #cccccc;"  # light gray
                "color: black;"  # dark text
                "font-weight: bold;"
                "padding: 4px;"
                "margin-bottom: 2px;"
            )
            self._container_layout.addWidget(header)

            # ---- Page Image ----
            page = self._doc.load_page(page_index)
            zoom = self._compute_fit_zoom(page) if self._fit_to_width else self._zoom
            pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)

            image = QImage(
                pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888
            )

            label = QLabel()
            label.setPixmap(QPixmap.fromImage(image))
            label.setAlignment(Qt.AlignCenter)

            self._container_layout.addWidget(label)
