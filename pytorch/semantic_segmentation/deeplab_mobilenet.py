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

plt.rcParams["savefig.bbox"] = 'tight'


def show(imgs):
    if not isinstance(imgs, list):
        imgs = [imgs]
    fix, axs = plt.subplots(ncols=len(imgs), squeeze=False)
    for i, img in enumerate(imgs):
        img = img.detach()
        img = F.to_pil_image(img)
        axs[0, i].imshow(np.asarray(img))
        axs[0, i].set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])

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

    model.eval()
    
    # ------------np.ndarray转为torch.Tensor------------------------------------
    # numpy image: H x W x C
    # torch image: C x H x W
    # np.transpose( xxx,  (2, 0, 1))   
    
    # img_cv = cv2.imread('E:\\Comm\\demo\\1.jpg',1)
    img_cv_s = cv2.imread('E:\\Comm\\demo\\5.jpg',1)
    img_cv = cv2.cvtColor(img_cv_s, cv2.COLOR_BGR2RGB)
    tensor_cv = torch.from_numpy(np.transpose(img_cv, (2, 0, 1))) # 将 H x W x C 转化为 C x H x W
    
    batch = convert_image_dtype(tensor_cv, dtype=torch.float) #将uint像素值归一化到0-1 float
    batch = batch.reshape([1, batch.shape[0], batch.shape[1], batch.shape[2]])
 
    #图像归一化处理
    normalized_batch = F.normalize(batch, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))

    predictions = model(normalized_batch)['out']
    
    #得到概率输出
    normalized_masks = torch.nn.functional.softmax(predictions, dim=1)

    # print(predictions)
    print(predictions.shape, predictions.min().item(), predictions.max().item())
    print(normalized_masks.shape)
    
    # dog_and_boat_masks = [
    # normalized_masks[img_idx, sem_class_to_idx[cls]]
    # for img_idx in range(batch.shape[0])
    # for cls in ('dog', 'boat', 'person')
    # ]
    
    # show(dog_and_boat_masks)
    # plt.show()
    
    
    result_person = normalized_masks[0][sem_class_to_idx['dog']]
    print(result_person.shape)
    result_person = result_person.detach().numpy()
    
    # result_person = result_person*255
    #像素的概率值大于0.5 的直接设为40
    result_person[result_person>=0.3] = 120
    result_person[result_person<0.3] = 0
    
    result_person = result_person.astype(np.uint8)
    # print(result_person)
    m_c_res = np.zeros((result_person.shape[0], result_person.shape[1], 3))
    m_c_res[:,:,0] = result_person
    
    img_cv_s = img_cv_s.astype(np.float32)/255.0
    m_c_res = m_c_res.astype(np.float32)/255.0
    img_cv_s[:,:,0] = img_cv_s[:,:,0] + m_c_res[:,:,0]
    cv2.imshow('demo', img_cv_s)
    cv2.waitKey()

