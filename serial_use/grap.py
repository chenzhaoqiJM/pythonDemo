
import serial
import serial.tools.list_ports
import cv2
import numpy as np

from MySerial import WriteSerial
            
if __name__ == "__main__": 
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #设备号为0
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
    
    
    img = np.ones([400,400,3],dtype=np.uint8)
    img = img*255
    save_flag = False
    index_count = 1;
    
    try:
        myserial =  WriteSerial()
        
        while True:
            if cap.isOpened() == False:
                print('can not open camera')
            
            serial_output = myserial.get_from_board() #从单片机获得串口输出
            print(serial_output)
            # print(type(serial_output))
            
            if serial_output == "KEY1按下\r\n":
                save_flag = True
                

            if save_flag == True:
                ret, frame = cap.read() #读取图像
                
                if ret == True:
                    print('save img to .....')
                    cv2.imwrite('C:\\Users\\hp\\Desktop\\images\\'+str(index_count)+'.jpg', frame) #按下Key1保存图片
                    index_count+=1
                    img = frame
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
