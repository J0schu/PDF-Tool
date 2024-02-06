from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QFormLayout, QFileDialog
from functions.pdf import get_author, get_creator, get_subject, get_title, add_metadata
from functions.fun import pathlist_to_str

class MetadataPage(QWidget):
    def __init__(self):
        super().__init__()

        # add input, output -> label and line edit
        metadata_button_input = QPushButton("open file")
        metadata_button_input.clicked.connect(self.metadata_input_clicked)
        self.metadata_file_label = QLabel()

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

        # build Layout
        formlayout= QFormLayout()
        formlayout.addRow(metadata_button_input, self.metadata_file_label)
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
    def button_write_metadate_clicked(self):
        if self.author_line_edit.text() == '':
            ret = QMessageBox.critical(self, "critical",
                                       "Select a PDF filename",
                                       QMessageBox.Ok)
        else:
            add_metadata(self.metadata_file_label.text(),
                          self.author_line_edit.text(),
                          self.creator_line_edit.text(),
                            self.subject_line_edit.text(),
                            self.title_line_edit.text())
    
    def metadata_input_clicked(self):
        dialog = QFileDialog()
        dialog.setNameFilter("*pdf")
        dialogSuccessful = dialog.exec()

        if dialogSuccessful:
            selectedFiles = dialog.selectedFiles()
            self.metadata_file_label.setText(pathlist_to_str(selectedFiles))
            
            self.author_line_edit.setText(get_author(pathlist_to_str(selectedFiles)))
            self.creator_line_edit.setText(get_creator(pathlist_to_str(selectedFiles)))
            self.subject_line_edit.setText(get_subject(pathlist_to_str(selectedFiles)))
            self.title_line_edit.setText(get_title(pathlist_to_str(selectedFiles)))