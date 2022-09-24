import numpy as np
import cv2
import time
import os
from PIL import Image



imgs_path =  r"C:\Users\hp\Desktop\4_aug\leftImg8bit"
tag_path =  r"C:\Users\hp\Desktop\4_aug\gtFine"

imgs_name = []
for _item in os.listdir(imgs_path):
    if _item.split('.')[-1] in ['jpg', 'png', 'bmp', 'jpeg']:
        imgs_name.append(_item)
read_flag = True
i=0
legth = len(imgs_name)
while(True):
    
    if read_flag:
        _name = imgs_name[i%legth]
        img = cv2.imread(os.path.join(imgs_path, imgs_name[i%legth]))
        anno = Image.open(os.path.join(tag_path, imgs_name[i%legth].split('.')[0]+'.png'))
        anno = np.array(anno)
        read_flag = False
    
    img_copy = img.copy()
    cv2.putText(img_copy, _name, (100,200), cv2.FONT_HERSHEY_COMPLEX,4,(255,0,255),15)
    img_copy = img_copy.astype(np.float32) / 255.0
    img_copy[anno!=0] = img_copy[anno!=0]+(0,0.2,0)
  
    cv2.namedWindow("FRAME", 0)
    cv2.namedWindow("src", 0)
    cv2.imshow('FRAME',img_copy)
    
    cv2.imshow('src', img)

    mykey = cv2.waitKey(30)
    if mykey & 0xFF == ord('a'):
        i = i-1
        read_flag = True
    if mykey & 0xFF == ord('d'):
        i = i+1
        read_flag = True
        
        
    if mykey & 0xFF == ord('q'):
        break
        