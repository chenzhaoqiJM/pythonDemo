import numpy as np
import cv2
import cMonocularMeasure

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

