from PySide6.QtWidgets import QWidget, QListWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog
from functions.pdf import merger
from functions.fun import pathlist_to_str

class MergerPage(QWidget):
    def __init__(self):
        super().__init__()

        self.pdfs = []
        self.output_name = ""

        # merger Page

        self.list = QListWidget()
        self.list.setStyleSheet('font-size: 14px;')

        self.label_input_name = QLabel("input filename")
        self.pdf_input_name = QLabel()
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

        # add Widgets to Page
        # add action buttons
        v_button_layout = QVBoxLayout()
        v_button_layout.addWidget(button_merge)
        v_button_layout.addWidget(button_up)
        v_button_layout.addWidget(button_down)
        v_button_layout.addWidget(button_remove)

        h_line_edit = QHBoxLayout()
        h_line_edit.addWidget(self.pdf_input_name)
        h_line_edit.addWidget(button_open)
        # add input, output -> label and line edit
        v_line_edit_layout = QVBoxLayout()
        v_line_edit_layout.addWidget(self.label_input_name)
        v_line_edit_layout.addLayout(h_line_edit)
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
            ret = QMessageBox.critical(self, "critical", 
                                   "Select at least two PDFs",
                                   QMessageBox.Ok)
            return
        else:
            self.output_name = self.pdf_output_name.text() + ".pdf"
            merger(self.pdfs, self.output_name)
            self.pdf_output_name.clear()
            self.list.clear()
            self.pdfs.clear()
    
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
        # self.pdfs.clear()
        # self.list.clear()
    
    def button_open_clicked(self):
        dialog = QFileDialog()
        dialog.setNameFilter("*pdf")
        dialogSuccessful = dialog.exec()

        if dialogSuccessful:
            selectedFiles = dialog.selectedFiles()
            self.list.addItem(pathlist_to_str(selectedFiles))

    def button_up_pressed(self):
        pass
