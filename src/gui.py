from PySide6.QtWidgets import QVBoxLayout, QTabWidget, QMainWindow
from widgets import MergerPage
from widgets import MetadataPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Merger")
        
        tab_widget = QTabWidget(self)
        tab_widget.setFixedWidth(640)
        tab_widget.setFixedHeight(480)
        
        # pages 
        merger_page = MergerPage()
        metadata_page = MetadataPage()

        # add pages to tabs 
        tab_widget.addTab(merger_page, "Merger")
        tab_widget.addTab(metadata_page, "Metadata Editor")
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)
