#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
# from cv2 import cv2
import cv2
import sys
import os
import pickle
import traceback


class CMonocularCalibration:

    def __init__(self):
        """相机的标定类，OpenCV的版本建议在4.5.0以上
        >>> 单目相机的标定相关函数都带有前缀名monocular
        """
        
        #**********************************************$#
        #以下为单目标定的变量
        self._monocular_path = ''
        self._monocular_images_path = []
        self._monocular_img_num_limit = 6
        self._monocular_image_width = 640
        self._monocular_image_height = 480
        self._monocular_chessCellLen = 24.6 #mm
        self._monocular_chessSize = [4,6]
        
        self._monocular_mode = 'square'
        self._monocular_file_flag = False
        self._monocular_image_ready = False
        self._monocularParameters = dict()
        self._monocular_calibration_finished = False
        
    #*************以下为单目相机的标定函数，主要得到相机的内参数、畸变向量等***************#
    def monocular_print(self):
        print('\n','Internal matrix is:', '\n', self._monocularParameters["cameraMatrix"], '\n')
        print('Distortion vector is:', '\n', self._monocularParameters["distCoeffs"], '\n')
    
    def monocular_from_file_read(self, path, c_file_name = 'monocular.npy'):
        self._monocularParameters  = np.load(os.path.join(path, c_file_name), allow_pickle=True).item()
    
    def monocular_set_calibration_images(self, path, c_file_name = 'monocular.npy' ,only_use_c_file = False,\
        num_limit=7, height=480, width=640, size=[4,6], length=24.6, mode = 'square'):
        """只针对单目标定；
        设置标定图像文件路径、标定好的文件名、是否只使用标定文件、图像数量、图像尺寸、标定板大小、单元实际长度mm
        """
        self._monocular_path = path
        self._monocular_img_num_limit = num_limit
        self._monocular_image_width = width
        self._monocular_image_height = height
        self._monocular_chessSize = size
        self._monocular_chessCellLen = length
        self._monocular_mode = mode
        
        
        listd = os.listdir(path) #检查文件夹下是否有指定数量的标定文件
        list_images = []
        for item in listd:
            k = item.split('.')[-1]
            if k == 'jpg' or k == 'jpeg' or k == 'png' or k=='bmp':
                list_images.append(item)
        if len(list_images)<num_limit:
            print("Calibration may fail because there are not enough pictures !!!") 
            
    

        #如果存在单目标定的文件就进行读取
        if listd.count( c_file_name )==1 :
            self.monocular_from_file_read(path, c_file_name)
            self._monocular_file_flag = True
            print('Your calibration file has been checked ^_^')
            if only_use_c_file == True: #仅仅使用标定文件且检测到标定文件就在此跳出
                return True
        else:
            print('Your calibration file was not detected')
            
        try:
            #读取制定数量的标定图片路径
            for i in range(0, len(list_images)):
                file_name = os.path.join(path, list_images[i])
                self._monocular_images_path.append(file_name)
        except :
            print('An error occurred. Please check the path or quantity of your pictures')   
            
            
    def monocular_calibration(self, c_file_name = 'monocular.npy', use_c_file = True):
        """只针对单目标定；
        >>> 形参：use_c_file设置为True表示尝试读取标定文件以避免重复标定，一般为True; c_file_name:存储相机参数文件名
        >>> 得到的标定参数的说明；注意：以列向量的形式组织
        >>> 相机内参：_monocularParameters["cameraMatrix"]； 畸变向量：_monocularParameters["distCoeffs"]
        >>>         矫正映射： _monocularParameters["map1"]； _monocularParameters["map2"]
        """
        if self._monocular_file_flag == True and use_c_file == True:
            print('you have calibrated for monocular !')
            self._monocular_calibration_finished = True
            return True
        
        if self._monocular_img_num_limit>len(self._monocular_images_path):
            print('There are not enough pictures to calibrate !!!')
            return False
        
        src_left = []
        try:
            #读取制定数量的标定图片
            for i in range(0, len(self._monocular_images_path)):
                file_name = self._monocular_images_path[i]
                img = cv2.imread(file_name, 1)
                leftg = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
                src_left.append(leftg)            
            self._monocular_image_ready = True
        except Exception as e:
            print(e)
            traceback.print_exc()

        if self._monocular_image_ready == False:
            print(" No calibration's images recevied !!, Please check your picture path and quantity Settings")
            return False  
        
        #棋盘格上角点的真实坐标
        objp = np.zeros((self._monocular_chessSize[0]*self._monocular_chessSize[1],3), np.float32)
        for i in range(0, self._monocular_chessSize[1]):#row
            for j in range(0, self._monocular_chessSize[0]): #col
                point = [j*self._monocular_chessCellLen, i*self._monocular_chessCellLen, 0.]
                objp[i*self._monocular_chessSize[0]+j][0] = point[0]
                objp[i*self._monocular_chessSize[0]+j][1] = point[1]
                objp[i*self._monocular_chessSize[0]+j][2] = point[2]
        apoints = objp
        
        
        # termination criteria， 迭代的终止条件
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        img_points_left = []
        objectpoints = [] #存储每一个棋盘格真实坐标的列表
        for i in range(0, len(src_left)):
            # Find the chess board corners
            col = self._monocular_chessSize[0]; row = self._monocular_chessSize[1]
            if self._monocular_mode == 'square':
                ret_l, corners_left = cv2.findChessboardCorners(src_left[i], (col,row), None)
            if self._monocular_mode == 'circle':
                flags = cv2.CALIB_CB_SYMMETRIC_GRID
                params = cv2.SimpleBlobDetector_Params()
                # params.maxCircularity = 1000
                params.maxArea = 100000
                blob = cv2.SimpleBlobDetector_create(params)
                pra = cv2.CirclesGridFinderParameters()
                ret_l, corners_left = cv2.findCirclesGrid(src_left[i], (col,row), flags, blob, pra)
                
            if(ret_l == True ):
                # corners_left = cv2.cornerSubPix(src_left[i],corners_left, (11,11), (-1,-1), criteria)
                img_points_left.append(corners_left)
                objectpoints.append(apoints)
        
        print('有效的标定板数量: ', len(img_points_left))
        if len(img_points_left) <= 2:
            print('标定板角点检测异常2345 !!!!!!!!!!!')
        # 标定摄像头
        ret_l, mtx_l, dist_l, rvecs_l, tvecs_l = cv2.calibrateCamera(
            objectPoints=objectpoints, imagePoints=img_points_left,imageSize=src_left[0].shape[::-1]
         , cameraMatrix=None, distCoeffs=None)
               
        self._monocularParameters["cameraMatrix"] = mtx_l; self._monocularParameters["distCoeffs"]=dist_l
        #存储参数文件
        np.save(os.path.join(self._monocular_path , c_file_name) , self._monocularParameters)
        
        # print("cameraMatrix", mtx_l.shape, type(mtx_l))
        # print("distCoeffs", dist_l.shape, type(dist_l))
        cv2.imwrite(os.path.join(self._monocular_path , 'cameraMatrix.tiff'), mtx_l.astype(np.float32) )
        cv2.imwrite(os.path.join(self._monocular_path , 'distCoeffs.tiff'), dist_l.astype(np.float32) )
        self._monocular_calibration_finished = True
        return True
    