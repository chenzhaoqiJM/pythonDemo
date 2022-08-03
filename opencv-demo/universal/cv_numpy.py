# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 14:39:03 2021

@author: zq
"""

import cv2
import numpy as np
from numpy.lib import scimath #可用于计算复数
import time

def my_fun(a):
    return (a[0]+a[1]+a[2])/3

img = cv2.imread('E:\\Comm\\demo\\5.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#480行，640列
img_n = np.full((480,640,3),[100,255,10], dtype=np.uint8)


img = img.astype(np.float32)/255.0 #转为高动态图

# img = np.apply_along_axis(my_fun, axis=2, arr=img) #转为灰度图
# img = -img + 1 #灰度值反转

####滤波示例
kernel_3x3 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])#高通滤波器核
gauss_kernel = np.array([[1,2,1],[2,4,2],[1,2,1]], dtype=np.float32) * 1/12.0 #高斯核，低通滤波器
sobel_kernel_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]], dtype=np.float32) * 1/8.0 #Sobel核，x方向
sobel_kernel_y = np.array([[1,2,1],[0,0,0],[-1,-2,-1]], dtype=np.float32) * 1/8.0 #Sobel核，y方向


t1 = time.time()
img_3x3 = ndimage.convolve(img, kernel_3x3)#没有opencv快速
print(time.time()-t1)
t1 = time.time()
img_3x3_cv2 = cv2.filter2D(img, -1, sobel_kernel_y) 
img_3x3_cv2 = np.abs(img_3x3_cv2) #取绝对值，将负梯度变为正
img_3x3_cv2  = (img_3x3_cv2-img_3x3_cv2.min())* 1.0/(img_3x3_cv2.max()-img_3x3_cv2.min()) #归一化到[0,1]
print(img_3x3_cv2.max(), img_3x3_cv2.min())
print(time.time()-t1)

###傅里叶变换示例
# img_n = np.fft.fft2(img)
# print("fft shape is", np.shape(img_n))
# print(img_n[0][0:10]) #打印10行看一看

# img_n = np.fft.ifft2(img_n)
# img_n = img_n.astype(np.float32)
# print(img_n[0][0:10]) #打印10行看一看

# print(img.shape)

cv2.imshow('zq', img)
cv2.imshow('zq2', img_3x3_cv2)
cv2.waitKey()