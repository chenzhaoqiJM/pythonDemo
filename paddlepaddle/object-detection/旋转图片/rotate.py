import numpy as np
import cv2
import time
import os
from PIL import Image
def rotate_and_resize_roi(img1, theta, scale_ratio=1):
    img = img1.copy()
    _rotateCenter = (np.shape(img)[1]//2, np.shape(img)[0]//2)#旋转中心
    _img_size = (np.shape(img)[1], np.shape(img)[0])#变换后的大小
    
    _R = cv2.getRotationMatrix2D(_rotateCenter, theta, scale_ratio) #计算旋转的仿射变换矩阵
    img_rotate = cv2.warpAffine(img, _R, _img_size)
    return theta, scale_ratio, img_rotate

src_imgs_path =  r'C:\Users\hp\Desktop\4_detection\images'
dst_imgs_path =  r"C:\Users\hp\Desktop\4_detection\0du"
bg_imgs_path = r"C:\Users\hp\Desktop\4_detection\bg"

imgs_name = []
for _item in os.listdir(src_imgs_path):
    if _item.split('.')[-1] in ['jpg', 'png', 'bmp', 'jpeg']:
        imgs_name.append(_item)
        
read_flag = True
i=0
legth = len(imgs_name)
theta=0
while(True):
    
    if read_flag:
        _name = imgs_name[i%legth]
        img = cv2.imread(os.path.join(src_imgs_path, _name))
        bg = cv2.imread(os.path.join(bg_imgs_path, _name))
        read_flag = False
    
    img_copy = img.copy()
    _theta, _scale, img_rotate = rotate_and_resize_roi(img, theta, scale_ratio=1)
    
    _img2_arr_mask1 = np.logical_and(img_rotate[:,:,0] == 0 , img_rotate[:,:,1] == 0) # 求R和G通道bool矩阵的交集
    img2_arr_mask = np.logical_and(_img2_arr_mask1, img_rotate[:,:,2] == 0)
    img_rotate[img2_arr_mask] = bg[img2_arr_mask]

  
    cv2.namedWindow("FRAME", 0)
    cv2.namedWindow("rotate", 0)
    cv2.imshow('FRAME',img_copy)
    
    cv2.imshow('rotate', img_rotate)

    mykey = cv2.waitKey(30)
    if mykey & 0xFF == ord('a'):
        i = i-1
        read_flag = True
    if mykey & 0xFF == ord('d'):
        i = i+1
        read_flag = True
    if mykey & 0xFF == ord('r'):
        theta = theta+1
        theta=theta%360
    if mykey & 0xFF == ord('t'):
        theta = theta-1
        theta=theta%360
    if mykey & 0xFF == ord('w'):
        cv2.imwrite(os.path.join(dst_imgs_path, _name), img_rotate)
    if mykey & 0xFF == ord('q'):
        break
        