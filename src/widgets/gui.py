from PySide6.QtWidgets import QMainWindow, QStackedWidget

from widgets.start_page import StartPage
from widgets.merger import Merger
from widgets.ocr import OCR


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Multi-Page App")
        self.resize(500, 400)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Create pages
        self.start_page = StartPage()
        self.merger_page = Merger()
        self.ocr_page = OCR()

        # Add to stack
        self.stack.addWidget(self.start_page)  # index 0
        self.stack.addWidget(self.merger_page)    # index 1
        self.stack.addWidget(self.ocr_page)    # index 2

        # Connect navigation signals
        self.start_page.go_page_merger.connect(lambda: self.stack.setCurrentIndex(1))
        self.start_page.go_page_ocr.connect(lambda: self.stack.setCurrentIndex(2))

        self.merger_page.go_home.connect(lambda: self.stack.setCurrentIndex(0))
        self.ocr_page.go_home.connect(lambda: self.stack.setCurrentIndex(0))

    #   tab_widget = QTabWidget(self)

        # pages 
        #merger_page = MergerPage()
        #metadata_page = MetadataPage()

        # add pages to tabs 
        #tab_widget.addTab(merger_page, "Merger")
        #tab_widget.addTab(metadata_page, "Metadata Editor")

        # menu bar
        #menu_bar = self.menuBar()
        #help_menu = menu_bar.addMenu("Help")
        #github_action = help_menu.addAction("GitHub")
        #github_action.triggered.connect(self.github_clicked)
        #about_action = help_menu.addAction("About")
        #about_action.triggered.connect(self.about_clicked)

        #self.setCentralWidget(tab_widget)
        
        # about messagebox content
        #osversion = platform.platform()
        #qtversion = PySide6.QtCore.__version__ 
        #self.about_text = """
        #Version : 1.0
        #Build : 12.02.24
        #Qt : """ + qtversion + """
        #OS : """ + osversion + """
        #                """

    #def about_clicked(self):
    #    ret = QMessageBox.about(self, "About",
    #                           self.about_text)
    #def github_clicked(self):
    #    webbrowser.open("https://github.com/J0schu/pdf_merger")
