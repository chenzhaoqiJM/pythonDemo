import numpy as np
import cv2
import time


img = cv2.imread('C:\\Users\\hp\\Desktop\\square\\1.jpg',1)

# img = cv2.imread('C:\\Users\\hp\\Desktop\\cv-picture\\zq\\new\\1-400r.bmp',1)

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_copy = img.copy()

#3.bmp
# threshold1 = 50
# threshold2 = 200

#1r.bmp, 螺柱直径的
threshold1 = 50
threshold2 = 200
index_tune= 0
index_circle = 0
while True:
    t0 = time.time()
    
    
    #腐蚀图像
    # img_erod = cv2.erode(img1, cv2.getStructuringElement(cv2.MORPH_RECT, (7,7)))
    
    # retval, img_binary = cv2.threshold(img1, 90, 255, cv2.THRESH_OTSU)
    retval, img_binary = cv2.threshold(img1, 150, 255, cv2.THRESH_BINARY) #3.bmp 花瓣、圆柱、顶圆
    # img_binary = cv2.dilate(img_binary, cv2.getStructuringElement(cv2.MORPH_RECT, (7,7)))
    # img2 = cv2.Canny(img_binary, threshold1, threshold2)
    img2 = cv2.Canny(img1, threshold1, threshold2)
    
    #霍夫圆检测
    # circles = cv2.HoughCircles(img1, cv2.HOUGH_GRADIENT, 1.5, 30, minRadius=300, maxRadius=500, param1=90, param2=90)
    # circles = cv2.HoughCircles(img1, cv2.HOUGH_GRADIENT, 1.5, 30, minRadius=3, maxRadius=200, param1=70, param2=80)
    circles = [[]]
    
    #找轮廓并发现最大轮廓
    contours, hierarchy	= cv2.findContours(img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = np.array(contours)
    contours_size = np.array([len(s) for s in contours ])
    sort_index = np.argsort(-contours_size) #返回从大到小的索引,降序排列
    idx = sort_index[index_tune] #取一个轮廓，按t增加索引

    img_copy = img.copy()
    cv2.drawContours(img_copy, contours, idx, (0,255,0), thickness=24)
    
    # for i in range(0,5):
    #     cv2.drawContours(img_copy, contours, sort_index[i], (0,255,0), thickness=24)
    
    #画检测到的圆
    if circles is not None:
        if len(circles[0])>0:
            print(circles.shape)
            # for item in circles[0]:
            #     cv2.circle(img_copy, (item[0], item[1]), item[2], (0,0,255), thickness=2)
            item = circles[0][index_circle]
            cv2.circle(img_copy, (item[0], item[1]), item[2], (255,0,0), thickness=20)
    
    print('total time cost = ', time.time()-t0)
    
    cv2.namedWindow('source',0);cv2.namedWindow('contours',0);cv2.namedWindow('binary',0);cv2.namedWindow('canny',0);
    cv2.imshow('source', img1)
    cv2.imshow('contours', img_copy)
    cv2.imshow('binary', img_binary)
    cv2.imshow('canny',img2)
    key = cv2.waitKey(100)
    
    if key == ord('t'):
        index_tune+=1
        if len(sort_index)-1 < index_tune:
            index_tune = len(sort_index)-1; print('已经是最后一个轮廓了')
    if key == ord('c'):
        index_circle+=1
        if len(circles[0])-1 < index_circle:
            index_circle = len(circles[0])-1; print('已经是最后一个圆了')
    if key == ord('a'):
        threshold1 = threshold1-1
    if key == ord('s'):
        threshold1 = threshold1+1
        
    if key == ord('d'):
        threshold2 = threshold2-1
    if key == ord('f'):
        threshold2 = threshold2+1
        
    if key == ord('q'):
        break