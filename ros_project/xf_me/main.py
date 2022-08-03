
# coding=utf8

import numpy as np
from cv2 import cv2
from ccalibration import CCameraCalibration

try:
    ros_env = True
    import rospy
except:
    ros_env = False
    print('NO MODULE Named rospy')

images_path_win = 'C:\\Users\\hp\\Desktop\\1280\\'
images_path_ros = '/home/zq/Desktop/1280/91/'
images_path = images_path_ros   #默认
win_mode = False


if ros_env == True:
    rospy.init_node('demo_mo', anonymous=False)
else:
    images_path = images_path_win
    win_mode = True

#初始化相机标定对象
mycc = CCameraCalibration()
mycc.monocular_set_calibration_images(images_path, 'monocular.npy', False, 14, 480, 640, [6,8], 22.0)
mycc.monocular_calibration('monocular.npy', True)

mycc.monocular_print()


cap = 0
if win_mode == True:
    cap = cv2.VideoCapture(1 , cv2.CAP_DSHOW)
else:
    cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):
    if cap.isOpened() == False:
        print('can not open camera')
        break
    ret, frame = cap.read()
    if ret == False:
        continue
    
    #畸变矫正
    dst = mycc.monocular_remap(frame)
    
    
    cv2.namedWindow("FRAME")
    cv2.imshow('FRAME',frame)

    # cv2.namedWindow("DST")
    cv2.imshow('DST',dst)
    
    mykey = cv2.waitKey(1)
    if mykey & 0xFF == ord('q'):
        
        break


# When everything done, release the capture
if ros_env == True:
    rospy.spin()
cap.release()
cv2.destroyAllWindows()


 