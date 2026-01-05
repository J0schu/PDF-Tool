from typing import cast

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QAbstractItemView,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from pdf_tool.functions.pdf import merge_pdfs
from pdf_tool.widgets.page_selector import PageSelector
from pdf_tool.widgets.pdf_preview import PdfPreview


class Merger(QWidget):

    go_home = Signal()

    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Files", "", "PDF Files (*.pdf)"
        )

        for path in files:
            item = QListWidgetItem()
            item.setData(Qt.UserRole, path)

            selector = PageSelector(path)
            item.setSizeHint(selector.sizeHint())

            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, selector)

    def merge(self):
        if self.list_widget.count() < 2:
            QMessageBox.critical(self, "Error", "Select at least two PDFs")
            return

        output, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "PDF Files (*.pdf)"
        )
        if not output:
            return
        if not output.lower().endswith(".pdf"):
            output += ".pdf"

        items = []

        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            selector = cast(PageSelector, self.list_widget.itemWidget(item))

            items.append(
                (
                    item.data(Qt.UserRole),
                    selector.get_mode(),
                    selector.get_custom_text(),
                )
            )

        merge_pdfs(items, output)

    def remove_file(self):
        self.preview.clear()
        self.list_widget.takeItem(self.list_widget.currentRow())

    def clear_list(self):
        self.preview.clear()
        self.list_widget.clear()

    def show_preview(self, item):
        self.preview.load_pdf(item.data(Qt.UserRole))

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Merger")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px;")

        # Horizontal Box with List and Preview
        list_prev = QHBoxLayout()

        self.list_widget = QListWidget()
        self.list_widget.setDragEnabled(True)
        self.list_widget.setAcceptDrops(True)
        self.list_widget.setDropIndicatorShown(True)
        self.list_widget.setDragDropMode(QAbstractItemView.InternalMove)
        self.list_widget.itemDoubleClicked.connect(self.show_preview)

        self.preview = PdfPreview()

        list_prev.addWidget(self.list_widget)
        list_prev.addWidget(self.preview)

        # Horizontal Box with Add and Merge Buttons
        button_layout1 = QHBoxLayout()

        btn_add = QPushButton("Add File")
        btn_add.clicked.connect(self.add_files)

        btn_merge = QPushButton("Merge")
        btn_merge.clicked.connect(self.merge)

        button_layout1.addWidget(btn_add)
        button_layout1.addWidget(btn_merge)

        # Horizontal Box with Remove and Clear Button
        button_layout2 = QHBoxLayout()

        btn_remove = QPushButton("Remove")
        btn_remove.clicked.connect(self.remove_file)

        btn_clear = QPushButton("Clear")
        btn_clear.clicked.connect(self.clear_list)

        button_layout2.addWidget(btn_remove)
        button_layout2.addWidget(btn_clear)

        # Back Button
        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.go_home.emit)

        bottom_layout = QHBoxLayout()

        bottom_layout.addWidget(back_btn)
        bottom_layout.addStretch()

        # Page Layout
        layout.addWidget(title)
        layout.addLayout(list_prev, stretch=2)
        layout.addLayout(button_layout1)
        layout.addLayout(button_layout2)
        layout.addLayout(bottom_layout)
