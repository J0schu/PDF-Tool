from PySide6.QtWidgets import QWidget, QListWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFormLayout
from functions.pdf import get_author, get_creator, get_subject, get_title, add_metadata

class MetadataPage(QWidget):
    def __init__(self):
        super().__init__()

        metadata_label_input = QLabel("input filename: ")
        self.metadata_line_edit_input = QLineEdit()
        self.metadata_line_edit_input.returnPressed.connect(self.metadata_input_return_pressed)

        author_label = QLabel("Author: ")
        self.author_line_edit = QLineEdit()

        creator_label = QLabel("Creator: ")
        self.creator_line_edit = QLineEdit()

        subject_label = QLabel("Subject: ")
        self.subject_line_edit = QLineEdit()

        title_label = QLabel("Title: ")
        self.title_line_edit = QLineEdit()

        button_write_metadate = QPushButton("Write Metadata")
        button_write_metadate.clicked.connect(self.button_write_metadate_clicked)

        formlayout= QFormLayout()
        formlayout.addRow(metadata_label_input, self.metadata_line_edit_input)
        formlayout.addRow(author_label, self.author_line_edit)
        formlayout.addRow(creator_label, self.creator_line_edit)
        formlayout.addRow(subject_label, self.subject_line_edit)
        formlayout.addRow(title_label, self.title_line_edit)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(formlayout)
        vbox2 = QVBoxLayout()
        vbox2.addWidget(button_write_metadate)
        vbox3 = QVBoxLayout()
        vbox3.addLayout(vbox1)
        vbox3.addLayout(vbox2)

        self.setLayout(vbox3)


    
    # metadata page functions
        
    def metadata_input_return_pressed(self):
        self.author_line_edit.setText(get_author(self.metadata_line_edit_input.text() + ".pdf"))
        self.creator_line_edit.setText(get_creator(self.metadata_line_edit_input.text() + ".pdf"))
        self.subject_line_edit.setText(get_subject(self.metadata_line_edit_input.text() + ".pdf"))
        self.title_line_edit.setText(get_title(self.metadata_line_edit_input.text() + ".pdf"))

    def button_write_metadate_clicked(self):
        add_metadata(self.metadata_line_edit_input.text() + ".pdf", self.author_line_edit.text(), self.creator_line_edit.text(), self.subject_line_edit.text(), self.title_line_edit.text())