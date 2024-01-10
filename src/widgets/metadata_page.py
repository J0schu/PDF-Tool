from PySide6.QtWidgets import QWidget, QListWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox


class MetadataPage(QWidget):
    def __init__(self):
        super().__init__()

        metadata_label_input = QLabel("input filename")
        self.metadata_line_edit_input = QLineEdit()

        self.author_line_edit = QLineEdit()

        v_metadata_layout = QVBoxLayout()
        v_metadata_layout.addWidget(metadata_label_input)
        v_metadata_layout.addWidget(self.metadata_line_edit_input)
        v_metadata_layout.addWidget(self.author_line_edit)

        self.setLayout(v_metadata_layout)


    
    # metadata page functions
    def test(self):
        pass