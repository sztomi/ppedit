from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('res/mainwindow.ui', self)

