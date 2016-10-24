from PyQt5.QtWidgets import QMainWindow, QFileDialog, QSplitter
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot

from .widgets import PPscratchPreview, Editor


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('res/mainwindow.ui', self)
        splitter = QSplitter(self)
        self.editor = Editor(self)
        self.scratcher = PPscratchPreview(self)
        splitter.addWidget(self.editor)
        splitter.addWidget(self.scratcher)
        self.scratcher.editor = self.editor
        self.editor.qpart.textChanged.connect(self.scratcher.update_preview)
        self.setCentralWidget(splitter)

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        filename, _ = QFileDialog.getOpenFileName(self, caption='Open a C++ header/source',
                                                  filter='C++ header/source (*.h *.hpp *.hh *hxx ' +
                                                         '*.i *.ipp *.ixx *.cpp *.cc *.cxx)')
        self.scratcher.target_file = filename
        try:
            with open(filename) as f:
                self.editor.qpart.text = f.read()
                self.editor.qpart.detectSyntax(language='C++')
        except FileNotFoundError:
            pass

    @pyqtSlot()
    def on_actionQuit_triggered(self):
        self.close()
