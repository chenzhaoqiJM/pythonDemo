
import sys
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QMainWindow
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent=parent)
        
        #设置窗口标题
        self.setWindowTitle('我的第一个窗口')
        
        #
        self.resize(500, 500)

        #
        self.status = self.statusBar()
        
        self.status.showMessage('5s 后关闭', 5000)
        
        self.center()
        
        
    
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        win_size = self.geometry()
        print(screen.width(), screen.height())
        left = (screen.width() - win_size.width())//2
        top = (screen.height() - win_size.height())//2
        self.move(left, top)
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('C:\\Users\\hp\\Desktop\\trian\\1.png'))

    mywindow = MyWindow()
    
    mywindow.show()
    
    sys.exit(app.exec_())
    