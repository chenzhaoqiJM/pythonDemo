# -*- coding: utf-8 -*-

from demo1 import Ui_MainWindow
import  sys
from PyQt5.QtWidgets import QWidget ,QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = Ui_MainWindow()

    MainWindow = QMainWindow()
    
    ui.setupUi(MainWindow)
    
    MainWindow.show()

    sys.exit(app.exec_())

    