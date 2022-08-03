import os
import random
import shutil

#生成具有层次结构的训练集
#cityformal类型数据

if __name__ == '__main__':
    base_path = 'E:\\datasets\\2\\zhujian\\' #数据集所在的根目录
    
    images_source_dir = 'leftImg8bit' #图片所在文件夹
    annotations_source_dir = os.path.join('leftImg8bit', 'annotations') #标签所在文件夹
    
    source_format = '.bmp'
    annotation_format = '.png'

    images_target_dir = 'images' #
    annotations_target_dir = 'annotations'
    
    train_ratio = 0.8; val_ratio = 0.1; test_ratio = 0.1
    images_second_dir = ['train', 'val', 'test']
    annotations_second_dir = ['train', 'val', 'test']
    
    #创建文件夹
    if not os.path.exists(os.path.join(base_path, images_target_dir)):
        os.makedirs(os.path.join(base_path, images_target_dir))
    if not os.path.exists(os.path.join(base_path, annotations_target_dir)):
        os.makedirs(os.path.join(base_path, annotations_target_dir))
    for image_sec, annotation_sec in zip(images_second_dir, annotations_second_dir):
        t1 = os.path.join(base_path, images_target_dir, image_sec)
        t2 = os.path.join(base_path, annotations_target_dir, annotation_sec)
        if not os.path.exists(t1):
            os.makedirs(t1)
        if not os.path.exists(t2):
            os.makedirs(t2)
            
    
    #获取文件名列表
    images_list = os.listdir(os.path.join(base_path, images_source_dir) )
    annotations_list_all = os.listdir(os.path.join(base_path, annotations_source_dir) )
    annotations_list = []
    #清除文件夹名字
    for item in annotations_list_all:
        if len(item)>=4 and item[-4:] == annotation_format:
            annotations_list.append(item)
    
    # print(images_list, annotations_list)
    #检查一下文件是否对应
    for item in annotations_list:
        if item.split('.')[0]+ source_format not in images_list:
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

    # print(val_images, val_annotations)
    #把图片放到训练集文件夹和训练集标签文件夹
    for image_file, annotation_file in zip(train_images, train_annotations):
        source_path = os.path.join(base_path, images_source_dir, image_file)
        dst_file = os.path.join(base_path, images_target_dir, images_second_dir[0])
        shutil.move(source_path, dst_file)
        
        source_path = os.path.join(base_path, annotations_source_dir, annotation_file)
        dst_path = os.path.join(base_path, annotations_target_dir, annotations_second_dir[0])
        shutil.move(source_path, dst_path)
        # print(image_file, annotation_file)
    
    #验证集 
    for image_file, annotation_file in zip(val_images, val_annotations):
        source_path = os.path.join(base_path, images_source_dir, image_file)
        dst_file = os.path.join(base_path, images_target_dir, images_second_dir[1])
        shutil.move(source_path, dst_file)
        
        source_path = os.path.join(base_path, annotations_source_dir, annotation_file)
        dst_path = os.path.join(base_path, annotations_target_dir, annotations_second_dir[1])
        shutil.move(source_path, dst_path)
    #
    #测试集
    for image_file, annotation_file in zip(test_images, test_annotations):
        source_path = os.path.join(base_path, images_source_dir, image_file)
        dst_file = os.path.join(base_path, images_target_dir, images_second_dir[2])
        shutil.move(source_path, dst_file)
        
        source_path = os.path.join(base_path, annotations_source_dir, annotation_file)
        dst_path = os.path.join(base_path, annotations_target_dir, annotations_second_dir[2])
        shutil.move(source_path, dst_path)
        