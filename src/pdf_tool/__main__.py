import sys

from PySide6.QtWidgets import QApplication

from pdf_tool.ui.gui import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
