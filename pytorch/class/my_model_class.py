# License: BSD
# Author: Sasank Chilamkurthy
import torch
import torch.nn as nn
import numpy as np
import torchvision
from torchvision import transforms

from torchvision.models import AlexNet, ResNet, MobileNetV2
import resnet50_vd
from typing import List, Optional, Callable

class myAlexNet(AlexNet):
    def __init__(self, num_classes: int = 1000, dropout: float = 0.5) -> None:
        super().__init__(num_classes, dropout)
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, 5),
        )
        
class myMobileNetV2(MobileNetV2):
    def __init__(self, num_classes: int = 1000, width_mult: float = 1, inverted_residual_setting: Optional[List[List[int]]] = None, round_nearest: int = 8, block: Optional[Callable[..., nn.Module]] = None, norm_layer: Optional[Callable[..., nn.Module]] = None, dropout: float = 0.2) -> None:
        super().__init__(num_classes, width_mult, inverted_residual_setting, round_nearest, block, norm_layer, dropout)
        self.classifier = nn.Sequential(nn.Dropout(0.2), nn.Linear(self.last_channel, 5))

class myHelper():
    # def __init__(self) -> None:
    #     pass
    @staticmethod
    def get_ResNet50_vd():
        model_rn = resnet50_vd.resnet50(pretrained=False, num_classes=1000) #若要加载预训练模型，类别必须设为1000
        num_rnrs = model_rn.top_in_features #最后一层的输入
        model_rn.fc = nn.Linear(num_rnrs, 5) #取代原网络的top层
        return model_rn