#!/usr/bin/env python
# coding=utf8

import numpy as np
import cv2
import sys
from mycalibration import ccalibration
from mymeasure import cMonocularMeasure

try:
    ros_env = True
    import rospy
except:
    ros_env = False
    print('NO MODULE Named rospy')

# images_path_win = 'C:\\Users\\hp\\Desktop\\cv-picture\\zq\\c3\\' 
images_path_win = 'C:\\Users\\hp\\Desktop\\cv-picture\\zq\\new\\c\\' 

images_path_ros = '/home/zq/Desktop/1280/91/'
images_path = images_path_ros   #默认
win_mode = False

if ros_env == True:
    rospy.init_node('demo_mo', anonymous=False)
else:
    images_path = images_path_win
    win_mode = True


#多张图片标定得到相机的内参与畸变向量
mycc = ccalibration.CCameraCalibration()
mycc.monocular_set_calibration_images(images_path, 'monocular.npy', False, 16, 720, 1280, [7,7], 5.0, mode='circle')
mycc.monocular_calibration('monocular.npy', True)
mycc.monocular_print()


mycmm = cMonocularMeasure.MonocularMeasure()
#对称圆标定板上圆的行数、列数
monocular_circleSize = [7,7]
monocular_circleCellLen = 5.0 #mm，圆心距


# imgpath = 'C:\\Users\\hp\\Desktop\\0.jpg' #测距用的单张标定图像，会标定出该平面上的外参数,该图不需要畸变矫正，pnp里面会做矫正的
# imgpath = 'C:\\Users\\hp\\Desktop\\cv-picture\\zq\\c3\\1.bmp' 
imgpath = 'C:\\Users\\hp\\Desktop\\cv-picture\\zq\\new\\c\\1.bmp'

#得到该标定图像中标定板上的圆心实际坐标与对应像素坐标
ret_l, world_points, pixel_points = mycmm.findCornersAndWorldPoints(singleImgPath=imgpath, 
                                                chessSize=monocular_circleSize, 
                                                chessCellLen=monocular_circleCellLen, mode='circle')
h, mask = cv2.findHomography( pixel_points, world_points[:,:-1],method=cv2.RANSAC)

#new c 总长
p0 = np.array([486, 843.6, 1], dtype=np.float32).reshape(3,1) 
p1 = np.array([1961, 872,1], dtype=np.float32).reshape(3,1)
#螺距长
# p0 = np.array([1051.4, 759.5, 1], dtype=np.float32).reshape(3,1) 
# p1 = np.array([1164, 761.7,1], dtype=np.float32).reshape(3,1)

#c3
# p0 = np.array([901, 900, 1], dtype=np.float32).reshape(3,1) #从畸变矫正后的图里面量取
# p1 = np.array([1681, 900,1], dtype=np.float32).reshape(3,1)

#高度变换后, 3.0为标定板厚度

# new c
h_low = -3.0 + 20.5  #底面到中心线高度

#c3
# h_low = -3.0 + 26.7 #到圆柱表面
# h_low = -3.0 + 14.73 #到花瓣
# h_low = -3.0 + 51.5 #到顶面螺柱圆


A = mycc._monocularParameters["cameraMatrix"]
distCoeff = mycc._monocularParameters["distCoeffs"]

h = mycmm.findHByPnPAndZDiff(A, distCoeff, world_points, pixel_points, zLow=h_low)
################################################

#求世界坐标平面上的齐次坐标，并做归一化(一般可以不用)
pt1 = h @ p0
pt1 = pt1/pt1[-1]

pt2 = h @ p1
pt2 = pt2/pt2[-1]

length = np.math.sqrt(np.sum((pt1-pt2)**2)) #求解两点长度


print('单应性矩阵H为 : ','\n', h, '\n')
print('第一个螺牙顶点和第五个螺牙顶点像素坐标: \n', p0.reshape(-1), p1.reshape(-1))
print('\n第一个螺牙顶点和第五个螺牙顶点的世界坐标: \n', pt1.reshape(-1), pt2.reshape(-1))
print('\n 四个螺距总长为 : ', length)
print('\n 螺距长为 : ', length/4.0)

