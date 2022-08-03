import torchvision
import torch
import cv2
import numpy as np
import torchvision.transforms.functional as F
from torchvision.transforms.functional import convert_image_dtype
import time

use_gpu = torch.cuda.is_available()

def draw_in_cvImg(img, positions_and_labels):
    for item in positions_and_labels:
        for  i, (position, tag, score) in enumerate(zip(item[0], item[1], item[2])) :
            cv2.rectangle(img, (int(position[0]), int(position[1])),
                          (int(position[2]), int(position[3]) ), color=(255, 255 , 200), 
                          thickness=3)
            cv2.putText(img, name_list[tag]+' '+ str(score)[:5], (int(position[0]), int(position[1])),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))
            


if __name__ == '__main__':
    COCO_INSTANCE_CATEGORY_NAMES = [
        '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
        'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
        'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
        'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
        'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
        'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
        'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
        'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
        'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
        'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
        'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
        'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
    ]
    name_list = COCO_INSTANCE_CATEGORY_NAMES
    
    # model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    model = torchvision.models.detection.fasterrcnn_mobilenet_v3_large_320_fpn(pretrained=True) #加载预训练模型
    # path = 'C:/Users/hp/.cache/torch/hub/ultralytics_yolov5_master'
    # model = torch.hub.load(path, 'yolov5s', source='local') 
    if use_gpu:
        model.cuda()
    model.eval() #设置为推理模式

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #设备号为0
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G')) #设置图片格式
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  #设置图片宽
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #设置高
    

    while True:
        if cap.isOpened() == False:
            print('can not')
            break
        ret, img_cv0 = cap.read()
        if ret == False:
            continue
            
        img_cv = cv2.cvtColor(img_cv0, cv2.COLOR_BGR2RGB) #转换颜色通道

        # ------------np.ndarray转为torch.Tensor------------------------------------
        # numpy image: H x W x C
        # torch image: C x H x W
        # np.transpose( xxx,  (2, 0, 1))   # 将 H x W x C 转化为 C x H x W
        tensor_cv = torch.from_numpy(np.transpose(img_cv, (2, 0, 1)))
        
        if use_gpu:
            tensor_cv = tensor_cv.cuda()
        
        x = convert_image_dtype(tensor_cv, dtype=torch.float) #将uint像素值归一化到0-1 float
        x = x.reshape([1, x.shape[0], x.shape[1], x.shape[2]]) #重映射一下形状，变成符合要求的输入
        
        #图像归一化处理
        # normalized_batch = F.normalize(x, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
        
        start = time.time()
        predictions = model(x)
        end = time.time()
        print('\n推理的耗时为{}s'.format(end-start))
        #[{}]类型
        
        score_threshold = .7    #设置得分阈值
        label_for_boxes = [
            [
            output['boxes'][output['scores'] > score_threshold].cpu().detach().numpy(), 
            output['labels'][output['scores'] > score_threshold].cpu().detach().numpy(),
            output['scores'][output['scores'] > score_threshold].cpu().detach().numpy()] 
            for output in predictions
        ]
        
        draw_in_cvImg(img_cv0, label_for_boxes) #画出检测结果
        
        cv2.namedWindow("frame")
        cv2.imshow('frame', img_cv0)

        mykey = cv2.waitKey(5)
        #按q退出循环，0xFF是为了排除一些功能键对q的ASCII码的影响
        if mykey & 0xFF == ord('q'):
            break

        
