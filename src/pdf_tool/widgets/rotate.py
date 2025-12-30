from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QLineEdit,
    QCheckBox
)
from PySide6.QtCore import (
    Signal,
    Qt
)
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtPdf import QPdfDocument


class Rotate(QWidget):
    go_home = Signal()

    def open_pdf(self):
        path, _ = QFileDialog.getOpenFileNames(self, "Select File", "", "PDF Files (*.pdf)")
        if path:
            self.path_label.setText(f"{path[0]}")
            self.pdf_doc.load(path[0])
            self.pdf_view.setDocument(self.pdf_doc)

    def on_checkbox_changed(self, checked: bool):
        self.input_label.setVisible(not checked)
        self.text_input.setVisible(not checked)

    def rotate_pdf(self):
        angle = self.angle_input.text()
        pass

    def save_pdf(self):
        pass

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Rotate")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px;")

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.go_home.emit)

        # middle Layout
        h_layout = QHBoxLayout()

        v_layout = QVBoxLayout()

        open_btn = QPushButton("Open")
        open_btn.clicked.connect(self.open_pdf)

        self.path_label = QLabel("No PDF Selected")

        checkbox = QCheckBox("Rotate all Pages")
        checkbox.setChecked(True)
        checkbox.toggled.connect(self.on_checkbox_changed)

        self.input_label = QLabel("Select which pages to rotate:\n (1-5, 8, 11-13)")
        self.input_label.setVisible(False)

        self.text_input = QLineEdit()
        self.text_input.setVisible(False)

        angle_label = QLabel("Angle:")

        angle_input = QLineEdit()

        self.angle_input = QLineEdit()
        self.angle_input.setVisible(False)

        rotate_btn = QPushButton("Rotate")
        rotate_btn.clicked.connect(self.rotate_pdf)

        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_pdf)

        self.pdf_view = QPdfView()
        self.pdf_doc = QPdfDocument()
        self.pdf_view.setDocument(self.pdf_doc)
        self.pdf_view.setPageMode(QPdfView.PageMode.MultiPage)

        v_layout.addWidget(open_btn)
        v_layout.addWidget(self.path_label)
        v_layout.addWidget(angle_label)
        v_layout.addWidget(angle_input)
        v_layout.addWidget(checkbox)
        v_layout.addWidget(self.input_label)
        v_layout.addWidget(self.text_input)
        v_layout.addWidget(self.angle_input)
        v_layout.addStretch()
        v_layout.addWidget(rotate_btn)
        v_layout.addWidget(save_btn)

        h_layout.addLayout(v_layout, stretch=1)
        h_layout.addWidget(self.pdf_view, stretch=3)

        # bottom Layout
        layout.addLayout(v_layout)
        bottom_layout = QHBoxLayout()

        bottom_layout.addWidget(back_btn)
        bottom_layout.addStretch()


        layout.addWidget(title)
        layout.addLayout(h_layout, stretch=2)
        layout.addStretch()
        layout.addLayout(bottom_layout)
