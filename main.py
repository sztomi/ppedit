import sys

from PyQt5.QtWidgets import QApplication, QStyleFactory
from ppedit.gui.windows import MainWindow
from resources import qInitResources, qCleanupResources

if __name__ == "__main__":
  app = QApplication(sys.argv)
  QApplication.setStyle(QStyleFactory.create("gtk2"))
  qInitResources()
  w = MainWindow()
  w.show()
  qCleanupResources()
  sys.exit(app.exec_())
