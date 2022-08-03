import sys
import os
import numpy as np
import random
from lxml import etree
import xml.dom.minidom as xmldom


if __name__ == '__main__':
    images_path = 'E:\\训练数据集\\train2\\images'
    base_path = 'E:\\训练数据集\\train2'
    annotations_path = 'E:\\训练数据集\\train2\\annotations'
    check_path = 'images'
    correct = False

    images_name_list = os.listdir(images_path)
    annotations_name_list = os.listdir(annotations_path)
    
    if(len(images_name_list) != len(annotations_name_list)):
        print('图片与标签的数量不一致，请检查是否有问题！！！')
    
    #下面用标签来检查是否有对应图片，以及图片名字和标签名字是否一样
    unqualified_count = 0
    for item in annotations_name_list:
        annotation_file_name = os.path.join(annotations_path, item)
        
        domobj = xmldom.parse(annotation_file_name)
        
        elementobj = domobj.documentElement
        subElementObjName = elementobj.getElementsByTagName("filename")
        subElementObjDir = elementobj.getElementsByTagName("folder")
        
        imageFileName = subElementObjName[0].firstChild.data
        imageFolder = subElementObjDir[0].firstChild.data
        if imageFileName in images_name_list and imageFolder==check_path:
            if correct == True:
                if item.split('.')[0] != imageFileName.split('.')[0]:
                    new_name = os.path.join(annotations_path, imageFileName.split('.')[0] + '.xml')
                    os.rename(annotation_file_name, new_name)
            continue
        else:
            unqualified_count+=1
            print('不合格的数据为：{}，不合格总数为：{}'.format(annotation_file_name, unqualified_count))
            #如果修改的标志为真
            if imageFileName not in images_name_list and imageFolder == check_path:
                print('在{}中没有与{}这个标签对应的图片'.format(imageFolder, annotation_file_name))
            if imageFileName in images_name_list and imageFolder != check_path:
                print('{}这个标签对应的图片在我们指定的{}文件夹下被找到，但是标签中的文件夹为{}'\
                    .format(annotation_file_name, check_path, imageFolder))
            if imageFileName not in images_name_list and imageFolder != check_path:
                print('没有在我们指定的文件夹下找到图片，且标签中文件夹名字错误')

                

    if unqualified_count == 0:
        print('数据集检查合格')
    else:
        print('数据集检查不合格')