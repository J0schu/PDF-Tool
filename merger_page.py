from PySide6.QtWidgets import QWidget, QListWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from pdf import merger

class MergerPage(QWidget):
    def __init__(self):
        super().__init__()

        self.pdfs = []
        self.output_name = ""

        # merger Page

        self.list = QListWidget()
        self.list.setStyleSheet('font-size: 14px;')

        self.label_input_name = QLabel("input filename")
        self.pdf_input_name = QLineEdit()
        self.pdf_input_name.returnPressed.connect(self.input_return_pressed)

        self.label_output_name = QLabel("output filename")
        self.pdf_output_name = QLineEdit()

        button_merge = QPushButton("Merge")
        button_merge.clicked.connect(self.button_merge_clicked)

        button_clear = QPushButton("Clear")
        button_clear.clicked.connect(self.button_clear_clicked)

        button_up = QPushButton("Up")

        button_down = QPushButton("Down")

        # add Widgets to Page
        # add action buttons
        v_button_layout = QVBoxLayout()
        v_button_layout.addWidget(button_merge)
        v_button_layout.addWidget(button_up)
        v_button_layout.addWidget(button_down)
        v_button_layout.addWidget(button_clear)

        # add input, output -> label and line edit
        v_line_edit_layout = QVBoxLayout()
        v_line_edit_layout.addWidget(self.label_input_name)
        v_line_edit_layout.addWidget(self.pdf_input_name)
        v_line_edit_layout.addWidget(self.label_output_name)
        v_line_edit_layout.addWidget(self.pdf_output_name)
        
        # build layout
        h_layout = QHBoxLayout()
        h_layout.addLayout(v_line_edit_layout)
        h_layout.addLayout(v_button_layout)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.list)

        self.setLayout(v_layout)

        # merger page functions
    def input_return_pressed(self):
        self.pdfs.append(self.pdf_input_name.text() + ".pdf")
        self.list.addItem(self.pdf_input_name.text() + ".pdf")
        self.pdf_input_name.clear()

    def button_merge_clicked(self):
        if len(self.pdfs) < 2:
            ret = QMessageBox.critical(self, "Message Title", 
                                   "Select at least two PDFs",
                                   QMessageBox.Ok)
            return
        self.output_name = self.pdf_output_name.text() + ".pdf"
        merger(self.pdfs, self.output_name)
        self.pdf_output_name.clear()
        self.list.clear()
        self.pdfs.clear()
    
    def button_clear_clicked(self):
        self.pdfs.clear()
        self.list.clear()
