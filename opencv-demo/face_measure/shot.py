
# coding=utf8
import numpy as np
import cv2
from cv2 import CALIB_CB_SYMMETRIC_GRID

#保存拍摄图片的路径
images_path_win = 'C:\\Users\\hp\\Desktop\\square\\' 
#按 w 保存图片到上面的路径，按 q 退出拍摄
#尽量在检测到标定点的时候按w保存图片，这样可以提高标定效果
mode = 'square'
mode = 'circle'
try:
    ros_env = True
    import rospy
except:
    ros_env = False
    print('NO MODULE Named rospy')
images_path_ros = '/home/zq/Desktop/1280/91/'   #linux下的
images_path = images_path_ros   #默认为linux系统
win_mode = False

#如果导入ros的相关包失败，则为win系统
if ros_env == True:
    pass
else:
    images_path = images_path_win
    win_mode = True


#初始化相机捕获类
cap = 0
if win_mode == True:
    cap = cv2.VideoCapture(1 , cv2.CAP_DSHOW)
else:
    cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#在显示的图像中，按下w键保存图像到images_path_win路径之下
#在角点被完全检测到的时候再保存
count = 1
while(True):
    if cap.isOpened() == False:
        print('can not open camera')
        break
    ret, frame = cap.read()
    if ret == False:
        continue
    print(frame.shape)
    
    #circle格的行数、列数
    if mode == 'circle':
        patternSize = (7,7)
        flags = CALIB_CB_SYMMETRIC_GRID #对称的圆网格
        retval, centers	=cv2.findCirclesGrid(frame, patternSize, flags) #检测圆心
    if mode == 'square':
        patternSize = (11,8)
        retval, centers	=cv2.findChessboardCorners(frame, patternSize)
    
    image = frame.copy()
  
    if retval:
        print(centers.shape)
        print(centers[0])
        image = cv2.drawChessboardCorners(image, patternSize, centers, retval) #画出角点
  
    cv2.namedWindow("FRAME")
    cv2.imshow('FRAME',frame)
    
    cv2.imshow('detect', image)

    mykey = cv2.waitKey(1)
    if mykey & 0xFF == ord('q'):
        break
    
    if mykey & 0xFF == ord('w'):
        cv2.imwrite(images_path+str(count)+'.jpg', frame)
        count+=1
        
# When everything done, release the capture
if ros_env == True:
    pass
cap.release()
cv2.destroyAllWindows()


 