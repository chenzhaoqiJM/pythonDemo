
import serial
import serial.tools.list_ports
import cv2
import numpy as np
import traceback

##global ser
class WriteSerial():
    def __init__(self):        
        self.serial_state = 'off' #串口状态

        plist = list(serial.tools.list_ports.comports()) #获取串口列表
        
        if len(plist) <= 0:
            print ("The Serial port can't find!")
            self.ser = 0
        else:
            plist_0 =list(plist[0])
            serialName = plist_0[0]
            # print(serialName)
            self.ser = serial.Serial(port=serialName,baudrate=9600, timeout = 5)
            self.serial_state = 'on'

    def get_from_board(self):
        if self.ser != 0 and self.ser.readable():
            try:
                text = self.ser.readline()
                # print(text.decode('gbk'))
                return text.decode('gbk')
            except :
                traceback.print_exc()
                self.serial_state = 'off'
                return ''
        else:
            print('Serial Init Failed!!!!!')
            return ''
        pass
    
    def write_to_board(self, txt='666'):
        if self.ser != 0:
            try:
                if self.ser.writable():
                    # self.ser.writelines(str(txt+'\\n').encode('gbk'))
                    self.ser.write(str(txt).encode('gbk'))
                    print('已写入')
            except :
                traceback.print_exc()
                self.serial_state = 'off'
        else:
            print('Serial Init Failed!!!!!')
        pass

    def shutdown(self):
        if self.ser != 0:
            self.ser.close()