from PySide6.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QListWidget
from pdf import merger


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Merger")

        self.pdfs = []
        self.output_name = ""

        self.list = QListWidget()
        self.list.setStyleSheet('font-size: 14px;')

        self.pdf_input_name = QLineEdit("enter input filename")
        self.pdf_input_name.returnPressed.connect(self.input_return_pressed)

        self.pdf_output_name = QLineEdit("enter output filename")
        self.pdf_output_name.returnPressed.connect(self.output_return_pressed)

        button_merge = QPushButton("Merge")
        button_merge.clicked.connect(self.button_merge_clicked)

        button_clear = QPushButton("Clear")
        button_clear.clicked.connect(self.button_clear_clicked)
        
        v_button_layout = QVBoxLayout()
        v_button_layout.addWidget(button_merge)
        v_button_layout.addWidget(button_clear)

        v_line_edit_layout = QVBoxLayout()
        v_line_edit_layout.addWidget(self.pdf_input_name)
        v_line_edit_layout.addWidget(self.pdf_output_name)
        
        h_layout = QHBoxLayout()
        h_layout.addLayout(v_line_edit_layout)
        h_layout.addLayout(v_button_layout)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.list)

        self.setLayout(v_layout)

    def input_return_pressed(self):
        self.pdfs.append(self.pdf_input_name.text() + ".pdf")
        self.list.addItem(self.pdf_input_name.text() + ".pdf")
        self.pdf_input_name.clear()

    def output_return_pressed(self):
        pass
    def button_merge_clicked(self):
        self.output_name = self.pdf_output_name.text() + ".pdf"
        merger(self.pdfs, self.output_name)
        self.pdf_input_name = "enter input filename"
        self.pdf_output_name = "enter output filename"
        self.list.clear()
        #self.pdfs.clear()
    
    def button_clear_clicked(self):
        self.pdfs.clear()
        self.list.clear()