
# coding=utf8
import numpy as np
from cv2 import cv2

try:
    ros_env = True
    import rospy
except:
    ros_env = False
    print('NO MODULE Named rospy')

images_path_win = 'C:\\Users\\hp\\Desktop\\1280\\' #保存拍摄图片的路径
images_path_ros = '/home/zq/Desktop/1280/91/'   #linux下的
images_path = images_path_ros   #默认为linux系统
win_mode = False

#如果导入ros的相关包失败，则为win系统
if ros_env == True:
    rospy.init_node('demo_mo', anonymous=False)
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
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

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
    
    #棋盘格的列数、行数
    chessSize = (6,8)
    ret_l, corners = cv2.findChessboardCorners(frame, chessSize, None) #检测角点
    
    image = frame.copy()
    image	=	cv2.drawChessboardCorners(image, chessSize, corners, ret_l) #画出角点
  
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
    rospy.spin()
cap.release()
cv2.destroyAllWindows()


 