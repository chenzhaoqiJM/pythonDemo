import torchvision
import torch
import cv2
import numpy as np
import torchvision.transforms.functional as F
from torchvision.transforms.functional import convert_image_dtype
import time

use_gpu = torch.cuda.is_available()

def draw_in_cvImg(img, positions_and_labels):
    cols = len(positions_and_labels['name']) #检测到的物体
    for i in range(0, cols):
        #一个一个取出来
        item = positions_and_labels.loc[i]
        #画矩形框
        cv2.rectangle(img, (int(item['xmin']), int(item['ymin'])),
                        (int(item['xmax']), int(item['ymax']) ), color=color_list[item['class']], 
                        thickness=3)
        #画物体类别和置信度
        cv2.putText(img, item['name']+' '+ str(item['confidence'])[:5], (int(item['xmin']), int(item['ymin'])),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))
            


if __name__ == '__main__':
    num_color = 108
    color_list = [(np.random.randint(0,255), np.random.randint(100,255), np.random.randint(170,255)) 
                  for i in range(0, num_color) ]
    
    path = 'C:/Users/hp/yolov5'
    # path = './'
    model = torch.hub.load(path, 'yolov5s', source='local') #从本地文件加载模型
    # model = torch.hub.load(path, 'yolov4.pth', source='local') #从本地文件加载模型
    #如果gpu可用则使用gpu
    if use_gpu:
        model.cuda()
    model.eval() #设置为推理模式

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #设备号为0
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G')) #设置图片格式
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  #设置图片宽
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #设置高
    

    while True:
        if cap.isOpened() == False:
            print('can not open camera')
            break
        ret, img_cv0 = cap.read()
        if ret == False:
            continue
            
        img_cv = cv2.cvtColor(img_cv0, cv2.COLOR_BGR2RGB) #转换颜色通道

        start = time.time()
        predictions = model(img_cv0)
        end = time.time()
        print('\n推理的耗时为{}s'.format(end-start))
        # print(dir(predictions))
        # print(predictions.imgs)
        # img = np.array(predictions.imgs)
        
 
 
        # 取出检测结果，pandas格式，每一帧只有一张图片，故索引为0
        positions_and_labels = predictions.pandas().xyxy[0]

        #只显示置信度大于0.5的物体
        threshold_me = 0.4
        positions_and_labels = positions_and_labels.loc[positions_and_labels['confidence']>=threshold_me]
        draw_in_cvImg(img_cv0, positions_and_labels)
     
        cv2.namedWindow("frame")
        cv2.imshow('frame', img_cv0)
        # cv2.imwrite('E:\\my.jpg', img_cv0)
        mykey = cv2.waitKey(5)
        #按q退出循环，0xFF是为了排除一些功能键对q的ASCII码的影响
        if mykey & 0xFF == ord('q'):
            break
        


        
