import sys
import os
import numpy as np
import random


if __name__ == '__main__':
    images_path = 'E:\\训练数据集\\tubel\\images'
    base_path = 'E:\\训练数据集\\tubel'
    annotations_path = 'E:\\训练数据集\\tubel\\annotations'

    images_name_list = os.listdir(images_path)
    annotations_name_list = os.listdir(annotations_path)
    
    if(len(images_name_list) != len(annotations_name_list)):
        print('图片与标签的数量不一致，请检查是否有问题！！！')
    
    train_ratio = 0.8
    val_ratio = 0.1
    test_ratio = 0.1
    
    #得到训练集等的大小
    val_size = int(val_ratio*len(images_name_list))
    test_size = int(test_ratio*len(images_name_list))
    train_size = len(images_name_list) - val_size - test_size
    
    train_images = []
    val_images = []
    test_images = []
    
    #按照比例划分数据集，以图片名字作为列表，在划分前应该检查标签与图片是否对应
    train_images = random.sample(images_name_list, train_size)
    #划分后从源数据集里面删除
    for item in train_images:
        images_name_list.remove(item)

    val_images = random.sample(images_name_list, val_size)
    for item in val_images:
        images_name_list.remove(item)
        
    test_images = images_name_list        
    
    # print(train_images)
    # print(val_images)
    # print(test_images)
    
    #检查我们的划分是否带来了重复元素
    set_list = set(train_images)
    if len(set_list) == len(train_images):
        print('元素没有重复')
     
    #保持训练集、开发集、测试集中标签对应的名字
    train_annotations_name= []
    val_annotations_name= []
    test_annotations_name= []
    
    #写入文件voc
    train_file_name = 'train.txt'  
    text_temp = '' 
    with open(os.path.join(base_path,train_file_name), 'wb') as f:
        for item in train_images:
            text_temp = './images/' + item + ' ' + './annotations/' + item.split('.')[0] + '.xml' + '\n'
            f.write(text_temp.encode())
            train_annotations_name.append(item.split('.')[0])
    
    val_file_name = 'valid.txt'  
    text_temp = '' 
    with open(os.path.join(base_path, val_file_name), 'wb') as f:
        for item in val_images:
            text_temp = './images/' + item + ' ' + './annotations/' + item.split('.')[0] + '.xml' + '\n'
            f.write(text_temp.encode())
            val_annotations_name.append(item.split('.')[0])
            
    test_file_name = 'test.txt'  
    text_temp = '' 
    with open(os.path.join(base_path, test_file_name), 'wb') as f:
        for item in test_images:
            text_temp = './images/' + item + ' ' + './annotations/' + item.split('.')[0] + '.xml' + '\n'
            f.write(text_temp.encode())
            test_annotations_name.append(item.split('.')[0])
            
    #将annotation的名字写入文件，便于生成coco数据集
    train_file_name_coco = 'train1.txt'
    text_temp = ''
    with open(os.path.join(base_path, train_file_name_coco), 'wb') as f:
        for item in train_annotations_name:
            text_temp = item + '\n'
            f.write(text_temp.encode())
    
    val_file_name_coco = 'valid1.txt'
    text_temp = ''
    with open(os.path.join(base_path, val_file_name_coco), 'wb') as f:
        for item in val_annotations_name:
            text_temp = item + '\n'
            f.write(text_temp.encode())
            
    test_file_name_coco = 'test1.txt'
    text_temp = ''
    with open(os.path.join(base_path, test_file_name_coco), 'wb') as f:
        for item in test_annotations_name:
            text_temp = item + '\n'
            f.write(text_temp.encode())