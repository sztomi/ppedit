from typing import List

from PyQt5.QtWidgets import QWidget, QSplitter, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.uic import loadUi

from qutepart import Qutepart

from ppedit.preprocessor import ClangPreprocessor



class PPscratchPreview(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.pp = ClangPreprocessor()
    self._flags = []

    splitter = QSplitter(self)
    splitter.setOrientation(Qt.Vertical)
    scratch_holder = QWidget(self)
    loadUi('res/scratch.ui', scratch_holder)
    self.scratch = scratch_holder.editor
    self.scratch.detectSyntax(language='C++')
    self.scratch.textChanged.connect(self.update_preview)

    preview_holder = QWidget(self)
    loadUi('res/preview.ui', preview_holder)
    self.preview = preview_holder.editor
    self.preview.detectSyntax(language='C++')

    splitter.addWidget(scratch_holder)
    splitter.addWidget(preview_holder)

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
    preprocessed = self.pp.get_preprocessed_contents(
        self.target_file, self.editor.qpart.text, self.scratch.text,
        self._flags)
    self.preview.text = preprocessed


class Editor(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.qpart = Qutepart(self)
    self.qpart.drawIndentations = False
    self.params_edit = QLineEdit(self)
    layout = QVBoxLayout()
    layout.setContentsMargins(2, 2, 2, 2)
    layout.addWidget(self.qpart)
    layout.addWidget(self.params_edit)
    self.setLayout(layout)
