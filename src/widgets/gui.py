import PySide6
from PySide6.QtWidgets import QTabWidget, QMainWindow, QMessageBox
from widgets.merger_page import MergerPage
from widgets.metadata_page import MetadataPage
import platform
import webbrowser


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF-Tool")

        tab_widget = QTabWidget(self)

        # pages 
        merger_page = MergerPage()
        metadata_page = MetadataPage()

        # add pages to tabs 
        tab_widget.addTab(merger_page, "Merger")
        tab_widget.addTab(metadata_page, "Metadata Editor")

        # menu bar
        menu_bar = self.menuBar()
        help_menu = menu_bar.addMenu("Help")
        github_action = help_menu.addAction("GitHub")
        github_action.triggered.connect(self.github_clicked)
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self.about_clicked)

        self.setCentralWidget(tab_widget)
        
        # about messagebox content
        osversion = platform.platform()
        qtversion = PySide6.QtCore.__version__ 
        self.about_text = """
        Version : 1.0
        Build : 12.02.24
        Qt : """ + qtversion + """
        OS : """ + osversion + """
                        """

    def about_clicked(self):
        ret = QMessageBox.about(self, "About",
                               self.about_text)
    def github_clicked(self):
        webbrowser.open("https://github.com/J0schu/pdf_merger")