from PyQt6.QtWidgets import *
from gui import *
import sys



class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submit_button.clicked.connect(lambda: self.submit())
        self.add_button.clicked.connect(lambda: self.add())
        self.reset_button.clicked.connect(lambda: self.reset())
        self.exit_button.clicked.connect(lambda: self.quit())

    def quit(self):
        sys.exit()

