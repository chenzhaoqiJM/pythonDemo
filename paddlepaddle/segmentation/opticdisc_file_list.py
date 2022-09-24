import os
import random
import shutil

#以指定比例在数据集根目录下生成对应的文件列表
#自定义Dateset或

if __name__ == '__main__':
    win_mode = False
    base_path = 'C:\\Users\\hp\\Desktop\\4_rect_1\\1024'
    
    images_source_dir = 'leftImg8bit'
    annotations_source_dir = 'gtFine'
    
    source_format = '.jpg'
    annotation_format = '.png'

    train_ratio = 0.9; val_ratio = 0.1; test_ratio = 0.0
            
    #获取源图片文件名列表
    images_list_all = os.listdir(os.path.join(base_path, images_source_dir) )
    images_list = []
    #清除文件夹名字
    for item in images_list_all:
        if len(item)>=4 and item.split('.')[-1] == source_format.split('.')[-1]:
            images_list.append(item)
    #获取标注图片文件名列表
    annotations_list_all = os.listdir(os.path.join(base_path, annotations_source_dir) )
    annotations_list = []
    #清除文件夹名字
    for item in annotations_list_all:
        if len(item)>=4 and item.split('.')[-1] == annotation_format.split('.')[-1]:
            annotations_list.append(item)
    
    #检查一下文件是否对应
    for item in annotations_list:
        if item.split('.')[0] + source_format not in images_list:
            print('标签{}未找到对应图片！！！！'.format(item))
            
    
    
    #计算训练集、测试集、开发集的大小     
    val_size = int(val_ratio * len(annotations_list))
    test_size = int(test_ratio * len(annotations_list))
    train_size = len(annotations_list) - val_size - test_size
    
    #--------开始划分---------#
    #*********训练集**********
    train_annotations = random.sample(annotations_list, train_size)
    train_images = []
    for item in train_annotations:
        train_images.append(item.split('.')[0]+ source_format)
    #划分后从源标签集里面删除
    for item in train_annotations:
        annotations_list.remove(item)
            
    #*********开发集**********
    val_annotations = random.sample(annotations_list, val_size)
    val_images = []
    for item in val_annotations:
        val_images.append(item.split('.')[0]+ source_format)
    #划分后从源标签集里面删除
    for item in val_annotations:
        annotations_list.remove(item)
            
    #**************验证集*************
    test_annotations = annotations_list
    test_images = []
    for item in test_annotations:
        test_images.append(item.split('.')[0]+ source_format)

    #
    seperate = '\\'
    if win_mode == False:
        seperate = '/'
    with open(os.path.join(base_path, 'train.txt'), 'wb') as f:
        for image, annotation in zip(train_images, train_annotations):
            line = images_source_dir + seperate + image + ' ' + annotations_source_dir + seperate + annotation 
            line = line + '\n'
            f.write(line.encode())
    with open(os.path.join(base_path, 'val.txt'), 'wb') as f:
        for image, annotation in zip(val_images, val_annotations):
            line = images_source_dir + seperate + image + ' ' + annotations_source_dir + seperate + annotation 
            line = line + '\n'
            f.write(line.encode())
    with open(os.path.join(base_path, 'test.txt'), 'wb') as f:
        for image, annotation in zip(test_images, test_annotations):
            line = images_source_dir + seperate + image + ' ' + annotations_source_dir + seperate + annotation 
            line = line + '\n'
            f.write(line.encode())

    