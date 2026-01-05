from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class StartPage(QWidget):
    go_page_merger = Signal()
    go_page_ocr = Signal()
    go_page_rotate = Signal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Start Page")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px;")

        btn_merger = QPushButton("Merger")
        btn_ocr = QPushButton("OCR")
        btn_rotate = QPushButton("Rotate")

        btn_merger.clicked.connect(self.go_page_merger.emit)
        btn_ocr.clicked.connect(self.go_page_ocr.emit)
        btn_rotate.clicked.connect(self.go_page_rotate.emit)

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(btn_merger)
        layout.addWidget(btn_ocr)
        layout.addWidget(btn_rotate)
        layout.addStretch()
