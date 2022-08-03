#!/usr/bin/env python
# coding=utf8

import numpy as np
import cv2
from mymeasure import cMonocularMeasure



mycmm = cMonocularMeasure.MonocularMeasure()
#对称圆标定板上圆的行数、列数
monocular_circleSize = [7,7]
monocular_circleCellLen = 5.0 #mm，圆心距

#棋盘格
# monocular_circleSize = [11, 8]
# monocular_circleCellLen = 3.0 #格子大小
mode = 'square'
mode = 'circle'

#测距用的单张标定图像，该图不需要畸变矫正
imgpath = 'C:\\Users\\hp\\Desktop\\square\\01.jpg' #yl

#得到该标定图像中标定板上的圆心实际坐标与对应像素坐标
ret_l, world_points, pixel_points = mycmm.findCornersAndWorldPoints(singleImgPath=imgpath, 
                                                chessSize=monocular_circleSize, 
                                                chessCellLen=monocular_circleCellLen, mode=mode)
h, mask = cv2.findHomography( pixel_points, world_points[:,:-1],method=cv2.RANSAC)


img = cv2.imread('C:\\Users\\hp\\Desktop\\square\\1.jpg',1)
img2 = cv2.Canny(img, 100, 200)
lines = cv2.HoughLines(img2, 1, np.math.pi/10, 230, 0, 0 )
if lines.any():
    print(lines.shape)
    #画出直线
    for i in range(0, len(lines)-1):
        rho = lines[i][0][0]; theta = lines[i][0][1];
        a = np.math.cos(theta); b = np.math.sin(theta);
        x0 = a * rho; y0 = b * rho;
        pt1 = [0,0] ; pt2 = [0,0]
        pt1[0] = int(x0 + 1000 * (-b));
        pt1[1] = int(y0 + 1000 * (a));
        pt2[0] = int(x0 - 1000 * (-b));
        pt2[1] = int(y0 - 1000 * (a));
        cv2.line(img, pt1, pt2, (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
    cv2.namedWindow('Line',0)
    cv2.imshow('Line', img)
    cv2.waitKey()

#zs
p0 = np.array([621.23, 51.36, 1], dtype=np.float32).reshape(3,1) #从畸变矫正后的图里面量取
p1 = np.array([553.85, 366.34,1], dtype=np.float32).reshape(3,1)

################################################

#求世界坐标平面上的齐次坐标，并做归一化(一般可以不用)
pt1 = h @ p0
pt1 = pt1/pt1[-1]

pt2 = h @ p1
pt2 = pt2/pt2[-1]

length = np.math.sqrt(np.sum((pt1-pt2)**2)) #求解两点长度

print('H Matrix : ','\n', h, '\n')
print('source point: ', p0.reshape(-1), p1.reshape(-1))
print('dst point: ', pt1.reshape(-1), pt2.reshape(-1))
print('\nlen: ', length)

