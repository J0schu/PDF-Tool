from PySide6.QtWidgets import QMainWindow, QStackedWidget

from pdf_tool.widgets.merger import Merger
from pdf_tool.widgets.ocr import OCR
from pdf_tool.widgets.rotate import Rotate
from pdf_tool.widgets.start_page import StartPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Tool")
        self.resize(500, 400)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Create pages
        self.start_page = StartPage()
        self.merger_page = Merger()
        self.ocr_page = OCR()
        self.rotate_page = Rotate()

        # Add to stack
        self.stack.addWidget(self.start_page)  # index 0
        self.stack.addWidget(self.merger_page)  # index 1
        self.stack.addWidget(self.ocr_page)  # index 2
        self.stack.addWidget(self.rotate_page)

        # Connect navigation signals
        self.start_page.go_page_merger.connect(lambda: self.stack.setCurrentIndex(1))
        self.start_page.go_page_ocr.connect(lambda: self.stack.setCurrentIndex(2))
        self.start_page.go_page_rotate.connect(lambda: self.stack.setCurrentIndex(3))

        self.merger_page.go_home.connect(lambda: self.stack.setCurrentIndex(0))
        self.ocr_page.go_home.connect(lambda: self.stack.setCurrentIndex(0))
        self.rotate_page.go_home.connect(lambda: self.stack.setCurrentIndex(0))
