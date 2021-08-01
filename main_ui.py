import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import mainwindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = mainwindow.Ui_mainwindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
