from PyQt5.QtGui import QPixmap
from MySerial import WriteSerial
from PyQt5.QtCore import QThread ,QMutex,pyqtSignal
import sys
import time
from Ui import Ui_MainWindow
from PyQt5.QtWidgets import QWidget ,QApplication, QMainWindow
import cv2
import numpy as np
from PIL import Image

class my():
#我们的初始化在这里进行 
    def __init__(self, MainWindow):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow) #初始化界面
        
        #sys slot
        self.ui.pushButtonClose.clicked.connect(MainWindow.close)
        
        self.set_Up_Demo() #初始化我们的内容、线程、串口、信号和槽、线程信号等

        self.save_image = False #保存图片的标志
        self.slide_angle = 0 #滑动条上一次的角度
        self.angleSum = 0 #电机从起始旋转的总角度
        
        self.th2Image = 0
        
    def set_Up_Demo(self):
        self.myserial =  WriteSerial() #初始化串口
        if self.myserial.ser != 0:
            self.ui.label_serial_state.setText("串口状态:串口已连接")
        else:
            self.ui.label_serial_state.setText("串口状态:串口初始化失败")
        
        # 当前线程id    
        print('main id', QThread.currentThread())
        
        self.thread_1 = Thread_1(self.myserial)  # 创建线程1
        self.thread_1._signal.connect(self.th1)  #线程发出信号连接到槽函数
        self.thread_1.start()   #开启线程

        self.thread_2 = Thread_2()  # 创建线程2
        self.thread_2._signal.connect(self.th2)  #线程发出信号连接到槽函数
        self.thread_2.start()   #开启线程
        

        
        #my slot
        self.ui.pushButtonForeward.clicked.connect(self.pushButtonForeward_slot) #电机正转一定角度的槽函数
        self.ui.pushButtonRollback.clicked.connect(self.pushButtonRollback_slot) #电机反转一定角度的槽函数
        self.ui.pushButtonResetMotor.clicked.connect(self.pushButtonResetMotor_slot) #电机回原点
        self.ui.horizontalSlider.sliderReleased.connect(self.horizontalSlider_slot1) #水平滑动条松开时进入槽函数

            
    def pushButtonForeward_slot(self, rev):
        angle = self.ui.spinBoxForeward.value()
        self.myserial.write_to_board(str(angle))
        self.angleSum += angle #正转180，加入总和
        
    def pushButtonRollback_slot(self, rev):
        angle = self.ui.spinBoxBack.value()
        self.myserial.write_to_board(str(-angle))
        self.angleSum += (-angle) 
        # print(rev)
    def pushButtonResetMotor_slot(self, rev):
        self.ui.label_slider.setText("正转角度:0")
        self.ui.horizontalSlider.setValue(0)
        ang = self.angleSum - int(self.angleSum/360.0)*360 #去掉旋转的360度
        if(abs(ang)>180):
            self.myserial.write_to_board("{}".format(ang/ang * (360-abs(ang)))) #写入串口,保持旋转方向不变
        else:
            self.myserial.write_to_board("{}".format(-ang))
        self.angleSum = 0
        self.slide_angle = 0
        
    
    def horizontalSlider_slot1(self):
        # print("#$$$$$$$$")
        val = self.ui.horizontalSlider.value() #读取滑动条值
        self.ui.label_slider.setText("正转角度:{}".format(val)) #更新标签的显示
        
        self.myserial.write_to_board("{}".format(val-self.slide_angle)) #写入串口
        self.angleSum += (val-self.slide_angle) #转过角度的总和加一下，用于电机归零
        self.slide_angle = val #更新滑动条值存储
        

        
    def th1(self, rev):
        print(rev)
        if rev[0] == "KEY1按下\r\n":
            self.save_image = True
        if rev[0] == "serial off":
            self.ui.label_serial_state.setText("串口状态:串口意外拔出")
        # self.ui.label.setText(rev[0])
        
    def th2(self, rev):
        print(self.thread_2.img.shape)
        if self.save_image == True:
            cv2.imwrite('C:\\Users\\hp\\Desktop\\images\\'+str(12)+'.jpg', self.thread_2.img) #按下Key1保存图片
            self.save_image = False
        im = Image.fromarray(cv2.cvtColor(self.thread_2.img, cv2.COLOR_BGR2RGB)) #从opencv到PIL的转换
        self.ui.label.setPixmap(QPixmap(im.toqpixmap())) #刷新图片显示
        
    def __del__(self):
        print("程序结束")
        self.myserial.shutdown()

#线程1 继承QThread 读串口
class Thread_1(QThread): 
    _signal = pyqtSignal(list) #线程要发出的信号格式
    def __init__(self, myserial):
        super().__init__()
        self.qmut_1 = QMutex() # 创建线程锁
        self.myserial = myserial #创建变量以便将serial传入run中

    def run(self):
        while(True):
            self.qmut_1.lock() # 加锁
            
            #检查串口的状态，是否为可用
            if self.myserial.serial_state == 'on':
                serial_output = self.myserial.get_from_board() #从单片机获得串口输出
                self._signal.emit([serial_output]) #将串口的输出发给主线程
            else:
                self._signal.emit(["serial off"]) #表示串口挂掉了
                self.myserial.__init__() #尝试再检测串口
            self.qmut_1.unlock() # 解锁
            time.sleep(0.1)
            

# 线程2，继承QThread， 捕获图像
class Thread_2(QThread):  
    _signal = pyqtSignal(bool)
    def __init__(self):
        super().__init__()
        self.qmut_2 = QMutex() # 创建线程锁
        self.cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) #设备号为0
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.img = np.ones([640,360,3],dtype=np.uint8)
        self.img = self.img*255
        
    def run(self):
        while(True):
            # self.qmut_2.lock() # 加锁
            if self.cap.isOpened() == False:
                print('can not open camera')
            ret, self.img = self.cap.read() #读取图像
            # ret,  mainimg= self.cap.read() #读取图像
            if ret == True:
                # cv2.namedWindow('zq')
                # cv2.imshow('zq', self.img)
            # cv2.waitKey(30)
            # self.qmut_2.unlock() # 解锁
                self._signal.emit(True)
            time.sleep(0.1)
            # self.sleep(0.1)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    MainWindow = QMainWindow()
    
    t = my(MainWindow)
    
    MainWindow.show()

    sys.exit(app.exec_())