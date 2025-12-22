from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal, Qt


class StartPage(QWidget):
    go_page_merger = Signal()
    go_page_ocr = Signal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Start Page")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px;")

        btn1 = QPushButton("Merger")
        btn2 = QPushButton("OCR")

        btn1.clicked.connect(self.go_page_merger.emit)
        btn2.clicked.connect(self.go_page_ocr.emit)

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addStretch()
