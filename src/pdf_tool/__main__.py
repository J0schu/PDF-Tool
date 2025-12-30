import sys

from PySide6.QtWidgets import QApplication

from pdf_tool.widgets.gui import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
