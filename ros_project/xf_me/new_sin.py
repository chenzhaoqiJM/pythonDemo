#!/usr/bin/env python
# coding=utf8

import numpy as np
import cv2
from ccalibration import CCameraCalibration
from cMonocularRec import  MonocularRec

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

#24.36
#初始化相机标定对象
mycc = CCameraCalibration()
mycc.monocular_set_calibration_images(images_path, 'monocular.npy', False, 12, 720, 1280, [6,8], 6.13)
mycc.monocular_calibration('monocular.npy', True)

mycc.monocular_print()



src_left = cv2.imread('C:\\Users\\hp\\Desktop\\1.jpg', 0)
#棋盘格上角点的真实坐标
_monocular_chessSize = [6,8]
_monocular_chessCellLen = 6.13 #mm

objp = np.zeros((_monocular_chessSize[0]*_monocular_chessSize[1], 3), np.float32)
for i in range(0, _monocular_chessSize[1]):#row
    for j in range(0, _monocular_chessSize[0]): #col
        point = [j*_monocular_chessCellLen, i*_monocular_chessCellLen, 0.]
        objp[i*_monocular_chessSize[0]+j][0] = point[0]
        objp[i*_monocular_chessSize[0]+j][1] = point[1]
        objp[i*_monocular_chessSize[0]+j][2] = point[2]
apoints = objp

# termination criteria， 迭代的终止条件
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

col = _monocular_chessSize[0]; row = _monocular_chessSize[1]
ret_l, corners_left = cv2.findChessboardCorners(src_left, (col,row), None)
if(ret_l == True ):
    # corners_left = cv2.cornerSubPix(src_left,corners_left, (11,11), (-1,-1), criteria)
    print('check!!!!!!!!!')
    pass

corners_left = corners_left.reshape(48,2)
h, mask = cv2.findHomography( corners_left, apoints[:,:-1],method=cv2.RANSAC)

p0 = np.array([527, 351, 1], dtype=np.float32).reshape(3,1)
p1 = np.array([1030, 450,1], dtype=np.float32).reshape(3,1)

# p0 = np.array([640, 354, 1], dtype=np.float32).reshape(3,1)
# p1 = np.array([677, 268,1], dtype=np.float32).reshape(3,1)

# p0 = np.array([555, 672, 1], dtype=np.float32).reshape(3,1)
# p1 = np.array([962, 516,1], dtype=np.float32).reshape(3,1)

#高度变换后
h_low = 0.0
# h_low = 23.9
# h_low = 10

A = mycc._monocularParameters["cameraMatrix"]
distCoeff = mycc._monocularParameters["distCoeffs"]
retvel, rvec, tvec = cv2.solvePnP(apoints, corners_left, cameraMatrix=A,distCoeffs=distCoeff)
W, jaconbin = cv2.Rodrigues(rvec)

W0 = W.copy()
W0[:,2] = tvec.reshape(-1) - h_low*W0[:,2]
H0 = A @ W0 #从实际坐标到像素坐标
H0 = np.linalg.inv(H0) #从像素坐标到实际坐标
H0 = H0 / H0[2][2] #齐次化最后一个参数
h = H0

################################################



pt1 = h @ p0
pt1 = pt1/pt1[-1]

pt2 = h @ p1
pt2 = pt2/pt2[-1]

length = np.math.sqrt(np.sum((pt1-pt2)**2))

print('H matrix is: ','\n', h, '\n')
print('source point: ', p0.reshape(-1), p1.reshape(-1))
print('dst point: ', pt1.reshape(-1), pt2.reshape(-1))
print('\nlen: ', length)

