
# coding=utf8
import numpy as np
from cv2 import CALIB_CB_SYMMETRIC_GRID
import cv2
from mycalibration import ccalibration

import os

#运行这个文件得到相机内参与畸变向量，并存储到标定文件
#标点完成后会开启摄像头，可以观察畸变矫正的效果，按 w 保存畸变矫正后的图片，按q退出

#标定图片或者标定文件所在的文件夹
images_path_win = 'C:\\Users\\hp\\Desktop\\10\\c\\' 
image_height = 720
image_width = 1280

#待矫正的图像
rectify_image_path = 'C:\\Users\\hp\\Desktop\\10\\1.bmp'
# rectify_image_path = ''

#畸变矫正后的图片保存路径
rectifySavePath = 'C:\\Users\\hp\\Desktop\\10\\1r.bmp'
if rectify_image_path != '':
    rectifySavePath = 'C:\\Users\\hp\\Desktop\\10\\1r.bmp'


#----------------------------------------------------------------------------------------------#分割线

images_path = images_path_win
win_mode = True

imgs_list = os.listdir(images_path)
num_sum = 0
for item in imgs_list:
    if len(item.split('.')) >= 2:
        k = item.split('.')[-1]
        if k == 'jpg' or k == 'png' or k=='bmp':
            num_sum = num_sum + 1
            temp_img = cv2.imread(os.path.join(images_path, item))
            image_width , image_height = temp_img.shape[0], temp_img.shape[1]
if num_sum < 8:
    print('你的标定板数量过少，请检查')
    

#初始化相机标定对象
mycc = ccalibration.CCameraCalibration()
mycc.monocular_set_calibration_images(images_path, 'monocular.npy', False, 
                                      num_sum, image_height, image_width, [7,7], 5.0, mode='circle')
# mycc.monocular_set_calibration_images(images_path, 'monocular.npy', False, 10, 720, 1280, [6,8], 6.13, mode='square')
mycc.monocular_calibration('monocular.npy', True)

mycc.monocular_print()

#初始化相机捕获类
cap = 0
if win_mode == True:
    cap = cv2.VideoCapture(1 , cv2.CAP_DSHOW)
else:
    cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#在显示的图像中，按下w键保存图像到images_path_win路径之下
#在角点被完全检测到的时候再保存
count = 1
while(True):
    if rectify_image_path == '':
        if cap.isOpened() == False:
            print('can not open camera')
            break
        ret, frame = cap.read()
        if ret == False:
            continue
    else:
        frame = cv2.imread(rectify_image_path, 0)
    # print(frame.shape)
    frame = mycc.monocular_remap(frame)
    
    #circle格的行数、列数
    patternSize = (7,7)
    flags = CALIB_CB_SYMMETRIC_GRID #对称的圆网格
    retval, centers	=cv2.findCirclesGrid(frame, patternSize, flags) #检测圆心
    
    image = frame.copy()
  
    if retval:
        print(centers.shape)
        print(centers[0])
        image = cv2.drawChessboardCorners(image, patternSize, centers, retval) #画出角点
  
    cv2.namedWindow("FRAME", 0)
    cv2.namedWindow('detect', 0)
    cv2.imshow('FRAME',frame)
    
    cv2.imshow('detect', image)

    mykey = cv2.waitKey(1)
    if mykey & 0xFF == ord('q'):
        break
    
    if mykey & 0xFF == ord('w'):
        cv2.imwrite(rectifySavePath, frame)
        count+=1
        
# When everything done, release the capture
if ros_env == True:
    pass
cap.release()
cv2.destroyAllWindows()


 