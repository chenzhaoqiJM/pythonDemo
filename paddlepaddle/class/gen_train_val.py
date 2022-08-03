import sys
import os
import numpy as np
import random
import shutil
from dataset_force import MyDataForce

if __name__ == '__main__':
    images_path = 'C:\\Users\\hp\\Desktop\\tire_dataset' #数据集路径
    annotations_path = 'C:\\Users\\hp\\Desktop\\tire_dataset' #标签文件保存的路径
    img_dir_list = ['bi', 'leb','li','normal'] #放置每种类别图片的文件夹
    
    img_copy_path = 'C:\\Users\\hp\\Desktop\\tire_dataset\\jpg' #最终放置图片的文件夹位置
    if not os.path.exists(img_copy_path):
        os.makedirs(img_copy_path)
    
    myforcer = MyDataForce() #数据集增强类
    myforcer.images_datasets_path = images_path #读取的数据集路径
    myforcer.img_force_path = 'C:\\Users\\hp\\Desktop\\tire_dataset\\new' #增广后的图片放置的位置
    myforcer.img_dir_list = img_dir_list #增广后图片放置的文件夹
    
    #设置比例、以及是否使用数据增广
    train_ratio = 0.7
    val_ratio = 0.2
    test_ratio = 0.1
    force_flag = True
    
    train_name_list = []
    val_name_list = []
    test_name_list = []
    name_list_total = []
    
    #将图片的文件名列表按比例进行划分，为生成标签准备
    #[0:bi, 1:leb, 2:li, 3:normal]
    for item in img_dir_list:
        path = os.path.join(images_path, item)
        tempImgNameList = os.listdir(path)
        trainSize  = int(len(tempImgNameList)* train_ratio)
        valSize = int(len(tempImgNameList)* val_ratio)
        testSize = len(tempImgNameList) - trainSize - valSize
        
        train_name_list.append(tempImgNameList[0:trainSize]) #文件名放入训练集
        val_name_list.append(tempImgNameList[trainSize:trainSize+valSize]) #文件名放入验证集
        test_name_list.append(tempImgNameList[trainSize+valSize: ]) #剩余的放入测试集
        
        name_list_total.append(tempImgNameList) #总的文件名
    
    #是否进行数据扩充
    if force_flag == True:
        #数据集扩充
        myforcer.name_list_total = train_name_list #只对训练集进行增广
        myforcer.generate_new_imgs()
        
        new_train_list = myforcer.get_new_name_list() #获取增广后的对应文件名
        
        #加入原来的训练集
        assert len(new_train_list) == len(train_name_list)
        for index, item in enumerate(new_train_list):
            train_name_list[index] = train_name_list[index]+ item  
            
        myforcer.move_imgs_to(os.path.join(images_path, 'jpg')) #将图片移动到/jpg这个文件夹下  

    train_file_name = 'train_list.txt'  
    text_temp = ''
    with open(os.path.join(annotations_path,train_file_name), 'wb') as f:
        #index 表示类别，item为每个类别文件名列表
        for index, item in enumerate(train_name_list):
            for subitem in item:
                text_temp = 'jpg/' + subitem + ' ' + str(index) + '\n'
                f.write(text_temp.encode())

    val_file_name = 'val_list.txt'  
    text_temp = ''
    with open(os.path.join(annotations_path,val_file_name), 'wb') as f:
        #index 表示类别，item为文件名
        for index, item in enumerate(val_name_list):
            for subitem in item:
                text_temp = 'jpg/' + subitem + ' ' + str(index) + '\n'
                f.write(text_temp.encode())

    test_file_name = 'test_list.txt'  
    text_temp = ''
    with open(os.path.join(annotations_path,test_file_name), 'wb') as f:
        #index 表示类别，item为该类别文件夹下的文件名列表
        for index, item in enumerate(test_name_list):
            for subitem in item:
                text_temp = 'jpg/' + subitem + ' ' + str(index) + '\n'
                f.write(text_temp.encode())

    #copy文件到jpg
    for names, imgdir in zip(name_list_total, img_dir_list):
        base = os.path.join(images_path, imgdir)
        for item in names:
            full_path = os.path.join(base, item)
            shutil.copy(full_path, os.path.join(images_path, 'jpg'))
    
    