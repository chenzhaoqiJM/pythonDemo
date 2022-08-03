# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 14:39:03 2021

@author: hp
"""

import torchvision
import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt

from torchvision.utils import draw_bounding_boxes
import torchvision.transforms.functional as F
from torchvision.transforms.functional import convert_image_dtype
import time

use_gpu = torch.cuda.is_available()


if __name__ == '__main__':
    sem_classes = [
        '__background__', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus',
        'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike',
        'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
    ]
    sem_class_to_idx = {cls: idx for (idx, cls) in enumerate(sem_classes)}
    
    #下载预训练模型
    model = torchvision.models.segmentation.deeplabv3_mobilenet_v3_large(
        pretrained=True
    )
    if use_gpu:
        model.cuda()

    model.eval()
    
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #设备号为0
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) 
    
    while(True):
        start = time.time()
        if cap.isOpened() == False:
            print('can not')
            break
        ret, img_cv_s = cap.read()
        if ret == False:
            continue

        img_cv = cv2.cvtColor(img_cv_s, cv2.COLOR_BGR2RGB)
        tensor_cv = torch.from_numpy(np.transpose(img_cv, (2, 0, 1))) # 将 H x W x C 转化为 C x H x W
        if use_gpu:
            tensor_cv = tensor_cv.cuda()
        
        batch = convert_image_dtype(tensor_cv, dtype=torch.float) #将uint像素值归一化到0-1 float
        batch = batch.reshape([1, batch.shape[0], batch.shape[1], batch.shape[2]])
    
        #图像归一化处理
        normalized_batch = F.normalize(batch, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))

        # if use_gpu:
        #     normalized_batch.cuda()
        predictions = model(normalized_batch)['out']
        
        #得到概率输出
        normalized_masks = torch.nn.functional.softmax(predictions, dim=1)

        
        
        result_person = normalized_masks[0][sem_class_to_idx['person']]

        #转换到numpy格式，可以放到后面一点
        result_person = result_person.cpu().detach().numpy()
        
        #像素的概率值大于0.5 的直接设为40
        threshold = 0.3
        result_person[result_person>= threshold] = 80.0/255.0
        result_person[result_person< threshold] = 0
        
        m_c_res = np.zeros((result_person.shape[0], result_person.shape[1], 3), dtype=np.float32)
        #将结果加入到蓝色通道，其它通道值全为0
        m_c_res[:,:,0] = result_person
        
        #转为浮点数高动态图像
        img_cv_s = img_cv_s.astype(np.float32)/255.0
        img_cv_s += m_c_res
        
        cv2.imshow('demo', img_cv_s)
        mykey = cv2.waitKey(5)
        #按q退出循环，0xFF是为了排除一些功能键对q的ASCII码的影响
        if mykey & 0xFF == ord('q'):
            break

        end = time.time()
        
        print('循环耗费时间为：{} s'.format(end-start))
        

