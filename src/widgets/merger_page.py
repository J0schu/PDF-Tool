from PySide6.QtWidgets import QWidget, QListWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog
from functions.pdf import merger
from functions.fun import pathlist_to_str

class MergerPage(QWidget):
    def __init__(self):
        super().__init__()

        self.pdfs = []

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
        button_down.pressed.connect(self.button_down_pressed)

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
    def button_merge_clicked(self):
        for x in range(self.list.count()):
          self.pdfs.append(self.list.item(x).text())
        if len(self.pdfs) < 2:
            ret = QMessageBox.critical(self, "critical", 
                                   "Select at least two PDFs",
                                   QMessageBox.Ok)
            self.pdfs.clear()
            return
        else:
            filename = QFileDialog.getSaveFileName(self,"Save File", "", "PDF File (*.pdf)")
            merger(self.pdfs, str(filename[0]) + ".pdf")
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