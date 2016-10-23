from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from qutepart import Qutepart


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('res/mainwindow.ui', self)
        self.statusBar()
        self.editor = Qutepart(self)
        self.setCentralWidget(self.editor)

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        QMessageBox.information(self, 'triggered!', 'actionOpen')


