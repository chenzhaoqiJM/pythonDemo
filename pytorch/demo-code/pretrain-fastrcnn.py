import torchvision
import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt

from torchvision.utils import draw_bounding_boxes
import torchvision.transforms.functional as F
from torchvision.transforms.functional import convert_image_dtype


name_list = ['']
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
def draw_taget_name(imgs, name_list):
    pass


plt.rcParams["savefig.bbox"] = 'tight'

def show(imgs, labels):
    if not isinstance(imgs, list):
        imgs = [imgs]
    fix, axs = plt.subplots(ncols=len(imgs), squeeze=False)
    for i, img in enumerate(imgs):
        img = img.detach()
        img = F.to_pil_image(img)
        axs[0, i].imshow(np.asarray(img))
        axs[0, i].set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])
        
        label = labels[i]
        # print(label)
        for  position, tag in zip(label[0], label[1]):
            axs[0,i].text(position[0], position[1], name_list[tag], color="b")
            # print(position[1])
            # print(tag)

model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
# For training
# images, boxes = torch.rand(4, 3, 600, 1200), torch.rand(4, 11, 4)
# labels = torch.randint(1, 91, (4, 11))
# images = list(image for image in images)
# targets = []
# for i in range(len(images)):
#     d = {}
#     d['boxes'] = boxes[i]
#     d['labels'] = labels[i]
#     targets.append(d)
# output = model(images, targets)
# # For inference
model.eval()

img_cv = cv2.imread('E:\\Comm\\demo\\8.jpg',1)
img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

img_cv2 = cv2.imread('E:\\Comm\\demo\\14.jpg',1)
img_cv2 = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
# print(img_cv.shape)
# print(np.transpose(img_cv, (2, 0, 1)).shape)


# ------------np.ndarray转为torch.Tensor------------------------------------
# numpy image: H x W x C
# torch image: C x H x W
# np.transpose( xxx,  (2, 0, 1))   # 将 H x W x C 转化为 C x H x W
tensor_cv = torch.from_numpy(np.transpose(img_cv, (2, 0, 1)))
tensor_cv2 = torch.from_numpy(np.transpose(img_cv2, (2, 0, 1)))


x1 = convert_image_dtype(tensor_cv, dtype=torch.float)
x2 = convert_image_dtype(tensor_cv2, dtype=torch.float)

x1 = torchvision.io.read_image('E:\\Comm\\demo\\8.jpg')
x2 = torchvision.io.read_image('E:\\Comm\\demo\\14.jpg')
x1 = convert_image_dtype(tensor_cv, dtype=torch.float)
x2 = convert_image_dtype(tensor_cv2, dtype=torch.float)
x = [x1, x2]

batch_int = [tensor_cv, tensor_cv2]
# batch_int = torch.stack([tensor_cv, tensor_cv2])
# batch = convert_image_dtype(batch_int, dtype=torch.float)

# x = [torch.rand(3, 300, 400), torch.rand(3, 500, 400)]

predictions = model(x)
# predictions = model(batch)


#画个框框示例一下
# boxes = torch.tensor([[50, 50, 100, 200], [210, 150, 350, 430]], dtype=torch.float)
# colors = ["blue", "yellow"]
# result = draw_bounding_boxes(tensor_cv, boxes, colors=colors, width=5)
# show(result)

score_threshold = .5
dogs_with_boxes = [
    draw_bounding_boxes(dog_int, boxes = output['boxes'][output['scores'] > score_threshold], width=4)
    for dog_int, output in zip(batch_int, predictions)
]
label_for_boxes = [
    [
     output['boxes'][output['scores'] > score_threshold].detach().numpy(), 
     output['labels'][output['scores'] > score_threshold].detach().numpy() ] 
    for dog_int, output in zip(batch_int, predictions)
]


# print(label_for_boxes)

show(dogs_with_boxes, label_for_boxes)

plt.show()
# optionally, if you want to export the model to ONNX:
# torch.onnx.export(model, x, "faster_rcnn.onnx", opset_version = 11)