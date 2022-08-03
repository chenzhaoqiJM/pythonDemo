import sys
import os
import numpy as np
import random
import shutil
import cv2

class MyDataForce():
    def __init__(self):
        self.images_datasets_path = 'C:\\Users\\hp\\Desktop\\tire_dataset'
        self.img_force_path = 'C:\\Users\\hp\\Desktop\\tire_dataset\\new'
        
        self.img_dir_list = ['bi', 'leb','li','normal']
        
        #如果不存在则创建文件夹
        for subdir in self.img_dir_list:
            if not os.path.exists(os.path.join(self.img_force_path, subdir)):
                os.makedirs(os.path.join(self.img_force_path, subdir))
        
        #旋转图像标志
        self.rotate_flag = True
        self.hist_flag = False
    
        self.name_list_total = []
        #[0:bi, 1:leb, 2:li, 3:normal]
        for item in self.img_dir_list:
            path = os.path.join(self.images_datasets_path, item)
            tempImgNameList = os.listdir(path)
            self.name_list_total.append(tempImgNameList)
    
    def generate_new_imgs(self):
        if self.rotate_flag == True or self.hist_flag == True:    
            #一个文件夹一个文件夹地增强
            for index, imgdir in enumerate(self.img_dir_list):
                count = 1 
                hist_count = 1
                tempPath = os.path.join(self.images_datasets_path, imgdir)
                for subitem in self.name_list_total[index]:
                    
                    if self.rotate_flag == True:
                        rotate_for_each = 2 #每一张图片旋转的次数
                        img = cv2.imread(os.path.join(tempPath, subitem), 1) #读入原图片
                        for t in range(rotate_for_each):
                            theta = np.random.randint(20, 340)
                            rotateCenter = (np.shape(img)[0]/2, np.shape(img)[1]/2)#旋转中心
                            img_size = (np.shape(img)[0], np.shape(img)[1])#变换后的大小
                            R = cv2.getRotationMatrix2D(rotateCenter, theta, 1) #计算旋转的仿射变换矩阵
                            img_rotate = cv2.warpAffine(img, R, img_size)
                            new_file_name = subitem[:-4]+imgdir+'_rotate_'+str(count)+str(t)+'.jpg' #文件名+源文件夹+变换标志+次数
                            cv2.imwrite(os.path.join(self.img_force_path, imgdir, new_file_name), img_rotate)
                            count+=1
                        
                    if self.hist_flag == True:
                        img = cv2.imread(os.path.join(tempPath, subitem), 1) #读入原图片
                        imgShape = (np.shape(img)[0], np.shape(img)[1], 1)
                        img_eHist0 = cv2.equalizeHist(img[:,:,0]) 
                        img_eHist1 = cv2.equalizeHist(img[:,:,1]) 
                        img_eHist2 = cv2.equalizeHist(img[:,:,2]) 
                        
                        img_eHist = np.concatenate([np.reshape(img_eHist0,imgShape), \
                            np.reshape(img_eHist1,imgShape), np.reshape(img_eHist2,imgShape)], axis=2)
                        new_file_name = subitem[:-4]+imgdir+'_hist_'+str(hist_count)+str(t)+'.jpg'
                        cv2.imwrite(os.path.join(self.img_force_path, imgdir, new_file_name), img_eHist)
                        hist_count+=1
        return True

    def get_new_name_list(self):
        #[0:bi, 1:leb, 2:li, 3:normal]
        name_list_total = []
        for item in self.img_dir_list:
            path = os.path.join(self.img_force_path, item)
            tempImgNameList = os.listdir(path)
            name_list_total.append(tempImgNameList)
        return name_list_total
    
    def move_imgs_to(self, dstImgDir):
        #copy文件到jpg
        name_list_total = self.get_new_name_list() #获得增广后的文件名列表
        for names, imgdir in zip(name_list_total, self.img_dir_list):
            base = os.path.join(self.img_force_path, imgdir) #得到每个类别文件夹的路径
            for item in names:
                full_path = os.path.join(base, item) #拼接得到单个文件的完全路径
                shutil.copy(full_path, dstImgDir)
        
if __name__ == '__main__':
                   
    myforcer = MyDataForce()
    myforcer.generate_new_imgs()

    
   
    
    