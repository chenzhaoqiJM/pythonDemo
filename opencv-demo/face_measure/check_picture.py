
# coding=utf8
import numpy as np
import cv2
from cv2 import CALIB_CB_SYMMETRIC_GRID

#保存拍摄图片的路径
images_path_win = 'C:\\Users\\hp\\Desktop\\Camcap_20220117_163034.bmp' 
#按 w 保存图片到上面的路径，按 q 退出拍摄
#尽量在检测到标定点的时候按w保存图片，这样可以提高标定效果

frame = cv2.imread(images_path_win, 0)
count = 1
while(True):
    print(frame.shape)
    
    #circle格的行数、列数
    patternSize = (7,7)
    flags = CALIB_CB_SYMMETRIC_GRID #对称的圆网格
    params = cv2.SimpleBlobDetector_Params()
    # params.maxCircularity = 80
    params.maxArea = 10000000
    blob = cv2.SimpleBlobDetector_create(params)
    pra = cv2.CirclesGridFinderParameters()
    flags = cv2.CALIB_CB_SYMMETRIC_GRID #对称的圆网格
    retval, centers	=cv2.findCirclesGrid(frame, patternSize, flags) #检测圆心
    
    image = frame.copy()
  
    if retval:
        print(centers.shape)
        print(centers[0])
        image = cv2.drawChessboardCorners(image, patternSize, centers, retval) #画出角点
        
    # ret, img_binary = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY) #
    # circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, 1.5, 30, minRadius=40, maxRadius=80, param1=140, param2=70)
    #画检测到的圆
    # if circles is not None:
    #     if len(circles[0])>0:
    #         print(circles.shape)
    #         for item in circles[0]:
    #             cv2.circle(image, (item[0], item[1]), item[2], (0,0,255), thickness=22)

  
    cv2.namedWindow("FRAME")
    cv2.namedWindow('detect',0)
    cv2.imshow('FRAME',frame)
    
    cv2.imshow('detect', image)

    mykey = cv2.waitKey(1)
    if mykey & 0xFF == ord('q'):
        break
    

cv2.destroyAllWindows()


 