from PySide6.QtWidgets import QApplication
import sys
from widgets.gui import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.setFixedWidth(640)
window.setFixedHeight(480)
window.show()

app.exec()