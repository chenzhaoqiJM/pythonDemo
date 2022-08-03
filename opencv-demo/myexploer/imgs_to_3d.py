import cv2
import numpy as np
import matplotlib.pyplot as plt

source_img = cv2.imread("C:\\Users\\86994\\Desktop\\flower-729512__340.jpg") # 读入图片
# plt.imshow(cv2.cvtColor(source_img, cv2.COLOR_BGR2RGB))
# plt.show()

data_img = source_img.reshape(-1,3)

_sub_data = data_img[0:]
fig = plt.figure(figsize=(15,15))#创建图片
subplot = fig.add_subplot(111, projection='3d')#确定函数图像位置，并标注绘制的是3D图（projection）
# Customize the z axis
subplot.set_xlim(0, 256)
subplot.set_ylim(0, 256)
subplot.set_zlim(0, 256)
sca = subplot.scatter(_sub_data[:,0],_sub_data[:,1],_sub_data[:,2])
plt.show()
