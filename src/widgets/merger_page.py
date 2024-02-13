from PySide6.QtWidgets import QWidget, QListWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog, QFormLayout
from functions.pdf import merger
from functions.fun import pathlist_to_str
import platform

class MergerPage(QWidget):
    def __init__(self):
        super().__init__()
        self.pdfs = []

        # merger Page
        self.list = QListWidget()
        self.list.setStyleSheet('font-size: 14px;')

        self.label_input = QLabel("Add Information:")

        button_open = QPushButton("open file")
        button_open.pressed.connect(self.button_open_clicked)

        self.label_output_name = QLabel("output filename")
        self.pdf_output_name = QLineEdit()

        button_merge = QPushButton("Merge")
        button_merge.clicked.connect(self.button_merge_clicked)

        button_remove = QPushButton("remove")
        button_remove.clicked.connect(self.button_remove_clicked)

        button_up = QPushButton("Up")
        button_up.pressed.connect(self.button_up_pressed)

        button_down = QPushButton("Down")
        button_down.pressed.connect(self.button_down_pressed)

        label_author = QLabel("Author")
        self.line_edit_author = QLineEdit()

        label_title = QLabel("Title")
        self.line_edit_title= QLineEdit()

        label_subject = QLabel("Subject")
        self.line_edit_subject = QLineEdit()

        label_keywords = QLabel("Keywords")
        self.line_edit_keywords = QLineEdit()

        formlayout = QFormLayout()
        formlayout.addRow(button_open, self.label_input)
        formlayout.addRow(label_author, self.line_edit_author)
        formlayout.addRow(label_title, self.line_edit_title)
        formlayout.addRow(label_subject, self.line_edit_subject)
        formlayout.addRow(label_keywords, self.line_edit_keywords)

        # add Widgets to Page
        # add action buttons
        v_button_layout = QVBoxLayout()
        v_button_layout.addWidget(button_merge)
        v_button_layout.addWidget(button_up)
        v_button_layout.addWidget(button_down)
        v_button_layout.addWidget(button_remove)

        v_information_box = QVBoxLayout()
        v_information_box.addLayout(formlayout)

        # build layout
        h_user_action = QHBoxLayout()
        h_user_action.addLayout(v_information_box)
        h_user_action.addLayout(v_button_layout)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_user_action)
        v_layout.addWidget(self.list)

        self.setLayout(v_layout)

        # merger page functions
    def button_merge_clicked(self):
        pdfname = ''
        for x in range(self.list.count()):
          self.pdfs.append(self.list.item(x).text())
        if len(self.pdfs) < 2:
            ret = QMessageBox.critical(self, "critical", 
                                   "Select at least two PDFs",
                                   QMessageBox.Ok)
            self.pdfs.clear()
            return
        filename = QFileDialog.getSaveFileName(self,"Save File", "", "PDF File (*.pdf)")
        if platform.system() == 'Windows':
            pdfname = str(filename[0])
        else:
            pdfname =str(filename[0]) + ".pdf"
        merger(self.pdfs, pdfname,
                self.line_edit_author.text(),
                self.line_edit_title.text(),
                self.line_edit_subject.text(),
                self.line_edit_keywords.text())
        self.list.clear()
        self.pdfs.clear()
        self.line_edit_author.clear(),
        self.line_edit_title.clear(),
        self.line_edit_subject.clear(),
        self.line_edit_keywords.clear()
    
    def button_remove_clicked(self):
        currentIndex = self.list.currentRow()
        item = self.list.item(currentIndex)
        if item is None:
            return
        question = QMessageBox.question(self, "remove Item",
                                        "Do you want to remove : " + item.text(),
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            item = self.list.takeItem(currentIndex)
            del item
    
    def button_open_clicked(self):
        dialog = QFileDialog()
        dialog.setNameFilter("*pdf")
        dialogSuccessful = dialog.exec()

        if dialogSuccessful:
            selectedFiles = dialog.selectedFiles()
            self.list.addItem(pathlist_to_str(selectedFiles))

    def button_up_pressed(self):
        index = self.list.currentRow()
        if index >= 1:
            item = self.list.takeItem(index)
            self.list.insertItem(index-1, item)
            self.list.setCurrentItem(item)
    def button_down_pressed(self):
        index = self.list.currentRow()
        if index < self.list.count()-1:
            item = self.list.takeItem(index)
            self.list.insertItem(index+1, item)
            self.list.setCurrentItem(item)