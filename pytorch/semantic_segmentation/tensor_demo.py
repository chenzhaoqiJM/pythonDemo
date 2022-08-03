import torchvision
import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt

from torchvision.utils import draw_bounding_boxes
import torchvision.transforms.functional as F
from torchvision.transforms.functional import convert_image_dtype
from torch.autograd import Variable


if __name__ == '__main__':

    normalize = torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
    
  
    # ------------np.ndarray转为torch.Tensor------------------------------------
    # numpy image: H x W x C
    # torch image: C x H x W
    # np.transpose( xxx,  (2, 0, 1))   # 将 H x W x C 转化为 C x H x W

    x1 = torchvision.io.read_image('E:\\Comm\\demo\\8.jpg')
    x1 = convert_image_dtype(x1, dtype=torch.float)
    x1 = x1.reshape([1,x1.shape[0], x1.shape[1], x1.shape[2]])
    
    print(x1.shape)
    
    # x1 = Variable(torch.unsqueeze(x1, dim=0).float(), requires_grad=False)
    # x = torch.tensor([0])
    # x[0] = x1
    print(x1.shape)


  

