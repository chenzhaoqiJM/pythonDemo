import sys
import os
import shutil

if __name__ == '__main__':
    
    #源图像文件夹的目录
    source_images_path = 'C:\\Users\\hp\\datasets\\coco2\\images_my'

    #标签的根目录
    labels_path = 'C:\\Users\\hp\\datasets\\coco2\\labels\\'
    
    #标签根目录下面的子目录
    labels_sub_path = ['train', 'valid', 'test']

    #复制的目标文件夹
    save_images_path = 'C:\\Users\\hp\\datasets\\coco2\\images'
    
    for i in range(0, len(labels_sub_path)):
        if not os.path.exists(os.path.join(save_images_path, labels_sub_path[i])):
            os.makedirs(os.path.join(save_images_path, labels_sub_path[i]))
            
        for item in os.listdir(os.path.join(labels_path, labels_sub_path[i]) ):
            name = item.split('.')[0] + '.jpg' #去掉.txt
            shutil.copy(os.path.join(source_images_path, name), os.path.join(save_images_path, labels_sub_path[i]))
    
    
    