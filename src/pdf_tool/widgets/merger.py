from PySide6.QtCore import Qt, Signal
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import (
    QAbstractItemView,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from pdf_tool.functions.pdf import merger


class Merger(QWidget):

    go_home = Signal()

    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Files", "", "PDF Files (*.pdf)"
        )
        self.list_widget.addItems(files)

    def merge(self):
        files = [
            self.list_widget.item(i).text() for i in range(self.list_widget.count())
        ]
        print(files)
        if len(files) < 2:
            ret = QMessageBox.critical(
                self, "critical", "Select at least two PDFs", QMessageBox.Ok
            )
            return
        user_mergename, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "PDF File (*.pdf)"
        )
        if user_mergename:
            mergename = user_mergename
            if not user_mergename.lower().endswith(".pdf"):
                mergename = user_mergename + ".pdf"
            merger(files, mergename)

    def remove_file(self):
        self.pdf_doc.load("")
        self.list_widget.takeItem(self.list_widget.currentRow())

    def clear_list(self):
        self.pdf_doc.load("")
        self.list_widget.clear()

    def show_preview(self, item):
        file_path = item.text()
        self.pdf_doc.load(file_path)
        self.pdf_view.setZoomMode(QPdfView.ZoomMode.FitToWidth)

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

        self.pdf_view = QPdfView()
        self.pdf_doc = QPdfDocument()
        self.pdf_view.setDocument(self.pdf_doc)
        self.pdf_view.setPageMode(QPdfView.PageMode.MultiPage)

        list_prev.addWidget(self.list_widget)
        list_prev.addWidget(self.pdf_view)

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
