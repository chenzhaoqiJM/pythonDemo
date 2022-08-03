
import serial
import serial.tools.list_ports
import cv2
import numpy as np


##global ser
class WriteSerial():
    def __init__(self):
        self.rear_v = 1500 
        self.steer_angle = 90

        plist = list(serial.tools.list_ports.comports()) #获取串口列表
        
        if len(plist) <= 0:
            print ("The Serial port can't find!")
            self.ser = 0
        else:
            plist_0 =list(plist[0])
            serialName = plist_0[0]
            # print(serialName)
            self.ser = serial.Serial(port=serialName,baudrate=9600, timeout = 60)

    def get_from_board(self):
        if self.ser != 0:
            text = self.ser.readline()
            # print(text.decode('gbk'))
            return text.decode('gbk')
        else:
            print('Serial Init Failed!!!!!')
            return ''
        pass
    
    def write_to_board(self, txt='666'):
        if self.ser != 0:
            if self.ser.writable():
                # self.ser.writelines(str(txt+'\\n').encode('gbk'))
                self.ser.write(str(txt).encode('gbk'))
                print('已写入')
        else:
            print('get Port Failed')
        pass

    def shutdown(self):
        if self.ser != 0:
            self.ser.close()
            


if __name__ == "__main__": 
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #设备号为0
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
    
    
    img = np.ones([400,400,3],dtype=np.uint8)
    img = img*255
    save_flag = False
    index_count = 1;
    
    try:
        myserial =  WriteSerial()
        print("INIT FULL")
        
        while True:
            if cap.isOpened() == False:
                print('can not open camera')
            else:
                ret, frame = cap.read() #读取图像
                

            serial_output = myserial.get_from_board() #从单片机获得串口输出
            print(serial_output)
            # print(type(serial_output))
            
            if serial_output == "KEY1按下\r\n":
                save_flag = True
                
            if ret == False: #检查图像读取情况
                print('failed to get img !')
            else:
                img = frame #更新图片到显示
                if save_flag == True:
                    print('save img to .....')
                    cv2.imwrite('C:\\Users\\hp\\Desktop\\'+str(index_count)+'.jpg', frame) #按下Key1保存图片
                    index_count+=1
                    save_flag = False
    
            cv2.imshow('zq',img)
            key = cv2.waitKey(3)
            
            if key == ord('w'):
                myserial.write_to_board("45")
            
            if key == ord('q'):
                break
            
        myserial.shutdown()
    except: 
        myserial.shutdown()
        print('some error ocurr!!!! Or user fouce to exit' )
