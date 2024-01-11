from PySide6.QtWidgets import QWidget, QListWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from functions import get_author, get_creator, get_subject, get_title

class MetadataPage(QWidget):
    def __init__(self):
        super().__init__()

        metadata_label_input = QLabel("input filename")
        self.metadata_line_edit_input = QLineEdit()
        self.metadata_line_edit_input.returnPressed.connect(self.metadata_input_return_pressed)

        self.author_line_edit = QLineEdit()

        v_metadata_layout = QVBoxLayout()
        v_metadata_layout.addWidget(metadata_label_input)
        v_metadata_layout.addWidget(self.metadata_line_edit_input)
        v_metadata_layout.addWidget(self.author_line_edit)

        self.setLayout(v_metadata_layout)


    
    # metadata page functions
    def metadata_input_return_pressed(self):
        self.author_line_edit.setText(get_author(self.metadata_line_edit_input.text() + ".pdf"))