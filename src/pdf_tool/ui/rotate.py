from PySide6.QtCore import Qt, Signal
from PySide6.QtPdf import QPdfDocument
from PySide6.QtWidgets import (
    QCheckBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from pdf_tool.functions.pdf import parse_pages, rotate_pdfs
from pdf_tool.widgets.pdf_preview import PdfPreview


class Rotate(QWidget):
    go_home = Signal()

    def open_pdf(self):
        path, _ = QFileDialog.getOpenFileNames(
            self, "Select File", "", "PDF Files (*.pdf)"
        )
        if path:
            self.path_label.setText(f"{path[0]}")
            self.preview.load_pdf(path[0])

    def on_checkbox_changed(self, checked: bool):
        self.input_label.setVisible(not checked)
        self.text_input.setVisible(not checked)

    def rotate_pdf(self):
        doc = self.preview._doc
        if not doc:
            QMessageBox.critical(self, "Error", "No PDF Selected")
            return
        if not self.angle_input.text():
            QMessageBox.critical(self, "Error", "Enter an angle")
            return

        try:
            angle = int(self.angle_input.text())
        except ValueError:
            angle = 90

        total_pages = doc.page_count
        if self.checkbox.isChecked():
            pages = list(range(total_pages))
        else:
            pages = parse_pages(self.text_input.text(), total_pages)

        rotate_pdfs(doc, angle, pages)
        self.preview._render()

    def save_pdf(self):
        doc = self.preview._doc
        if not doc:
            QMessageBox.critical(self, "Error", "No PDF to save")
            return
        path, _ = QFileDialog.getSaveFileName(
            self, "Save Rotated File", "", "PDF Files (*.pdf)"
        )
        if path:
            doc.save(path)

    def clear_pdf(self):
        self.preview.clear()
        self.input_label.setVisible(False)
        self.text_input.setVisible(False)
        self.angle_input.setPlaceholderText("90")
        self.angle_input.setText("")
        self.text_input.setText("")
        self.checkbox.setChecked(True)
        self.path_label.setText("No PDF Selected")

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

        self.checkbox = QCheckBox("Rotate all Pages")
        self.checkbox.setChecked(True)
        self.checkbox.toggled.connect(self.on_checkbox_changed)

        self.input_label = QLabel("Select which pages to rotate:\n (1-5, 8, 11-13)")
        self.input_label.setVisible(False)

        self.text_input = QLineEdit()
        self.text_input.setVisible(False)

        angle_label = QLabel("Angle:")

        self.angle_input = QLineEdit()
        self.angle_input.setPlaceholderText("90")

        btn_rotate = QPushButton("Rotate")
        btn_rotate.clicked.connect(self.rotate_pdf)

        btn_save = QPushButton("Save")
        btn_save.clicked.connect(self.save_pdf)

        btn_clear = QPushButton("Clear")
        btn_clear.clicked.connect(self.clear_pdf)

        self.preview = PdfPreview()
        self.pdf_doc = QPdfDocument()

        v_layout.addWidget(open_btn)
        v_layout.addWidget(self.path_label)
        v_layout.addWidget(angle_label)
        v_layout.addWidget(self.angle_input)
        v_layout.addWidget(self.checkbox)
        v_layout.addWidget(self.input_label)
        v_layout.addWidget(self.text_input)
        v_layout.addStretch()
        v_layout.addWidget(btn_rotate)
        v_layout.addWidget(btn_save)
        v_layout.addWidget(btn_clear)

        h_layout.addLayout(v_layout, stretch=1)
        h_layout.addWidget(self.preview, stretch=2)

        # bottom Layout
        layout.addLayout(v_layout)
        bottom_layout = QHBoxLayout()

        bottom_layout.addWidget(back_btn)
        bottom_layout.addStretch()

        layout.addWidget(title)
        layout.addLayout(h_layout, stretch=2)
        layout.addStretch()
        layout.addLayout(bottom_layout)
