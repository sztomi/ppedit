from PyQt5.QtWidgets import QWidget, QSplitter, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt, pyqtSlot
from qutepart import Qutepart

from ppedit.preprocessor import ClangPreprocessor

from typing import List


class PPSketchPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pp = ClangPreprocessor()
        self._flags = []
        splitter = QSplitter(self)
        splitter.setOrientation(Qt.Vertical)
        self.sketch = Qutepart(self)
        self.sketch.detectSyntax(language='C++')
        self.sketch.textChanged.connect(self.update_preview)
        self.preview = Qutepart(self)
        self.preview.detectSyntax(language='C++')
        splitter.addWidget(self.sketch)
        splitter.addWidget(self.preview)
        layout = QVBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.addWidget(splitter)
        self.setLayout(layout)

    @property
    def flags(self):
        return self._flags

    @flags.setter
    def flags(self, flags: List[str]):
        self._flags = flags
        self.update_preview()

    @pyqtSlot()
    def update_preview(self):
        preprocessed = self.pp.get_preprocessed_contents(self.target_file, self.editor.qpart.text, self.sketch.text,
                                                         self._flags)
        self.preview.text = preprocessed


class Editor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.qpart = Qutepart(self)
        self.params_edit = QLineEdit(self)
        layout = QVBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.addWidget(self.qpart)
        layout.addWidget(self.params_edit)
        self.setLayout(layout)
