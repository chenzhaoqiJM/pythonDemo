

import cv2
import numpy as np
import time
import threading

class MyThreadCamera(threading.Thread):
    def __init__(self, threadID, name, count):
        super(MyThreadCamera, self).__init__()
        self.threadID = threadID
        self.name = name
        self.counter = count
            
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #设备号为0
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
        # self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.image = np.ones([400,400,3],dtype=np.uint8)
        self.exit_flag = False
        
    def run(self):
        print("ThreadCamera start to running")
        while True:
            if self.cap.isOpened() == False:
                print('can not open camera!!!!!')
            else:
                ret, self.image = self.cap.read() #读取图像
            time.sleep(0.1)
            if self.exit_flag == True:
                break
            
            
if __name__ == "__main__": 

    myCameraThread = MyThreadCamera(0, "camera_thread", 0)
    myCameraThread.start()
    # myCameraThread.join()
    #join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程再终止
    
    img = np.ones([400,400,3],dtype=np.uint8)
    img = img*255
    save_flag = False
    index_count = 1;
    try:
        while True:   
            img = myCameraThread.image     
            if save_flag == True:
                # img = myCameraThread.image
                save_flag = False
            cv2.imshow('zq',img)
            
            key = cv2.waitKey(10)
            
            if key == ord('p'):
                save_flag = True
            if key == ord('q'):
                myCameraThread.exit_flag = True
                break

    except: 

        print('some error ocurr!!!! Or user fouce to exit' )
