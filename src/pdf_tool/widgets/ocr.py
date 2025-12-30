from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal, Qt


class OCR(QWidget):
    go_home = Signal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("OCR")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px;")

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.go_home.emit)


        bottom_layout = QHBoxLayout()

        bottom_layout.addWidget(back_btn)
        bottom_layout.addStretch()


        layout.addWidget(title)
        layout.addStretch()
        layout.addLayout(bottom_layout)
