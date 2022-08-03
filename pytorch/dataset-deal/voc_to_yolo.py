import sys
import os
import numpy as np
import random
from lxml import etree
import xml.dom.minidom as xmldom
import shutil

if __name__ == '__main__':
    images_path = 'E:\\训练数据集\\train2\\images'
    base_path = 'E:\\训练数据集\\train2'
    annotations_path = 'E:\\训练数据集\\train2\\annotations'
    
    save_base_path = 'E:\\训练数据集\\train-yolo'
    save_images_path = 'E:\\训练数据集\\train-yolo\\images'
    save_labels_path = 'E:\\训练数据集\\train-yolo\\labels'
    if not os.path.exists(save_base_path):
        os.mkdir(save_base_path)
    if not os.path.exists(save_images_path):
        os.mkdir(save_images_path)
        
    
    images_name_list = os.listdir(images_path)
    annotations_name_list = os.listdir(annotations_path)
    
    for image_file_name in images_name_list:
        try:
            shutil.copy(os.path.join(images_path, image_file_name), save_images_path)
        except :
            print('copy images failed!!!')
        
    #取标签文件，计算新边框
    for annotation_file_name in annotations_name_list:
        try:
            annotation_file = os.path.join(annotations_path, annotation_file_name)
            domobj = xmldom.parse(annotation_file)
        
            elementobj = domobj.documentElement
            subElementObjName = elementobj.getElementsByTagName("filename")
            subElementObjDir = elementobj.getElementsByTagName("folder")
            
            imageFileName = subElementObjName[0].firstChild.data
            imageFolder = subElementObjDir[0].firstChild.data
            pass
        except :
            pass
    
    
    
    
    