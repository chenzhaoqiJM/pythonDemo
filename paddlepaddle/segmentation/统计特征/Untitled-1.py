# %%
import numpy as np
import cv2
import time
import os
from PIL import Image
import matplotlib.pyplot as plt

# %%
img = Image.open(r'C:\Users\hp\Desktop\4_rect_1\1024\leftImg8bit\1.jpg')
img = np.array(img)

# %%
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.resize(img_gray, (200, 200))

# %%
plt.imshow(img_gray,cmap='gray')

# %%
x = np.linspace(0, img_gray.shape[0]-1, img_gray.shape[0]).astype(np.int32)
y = np.linspace(0, img_gray.shape[1]-1, img_gray.shape[1]).astype(np.int32)
x1, y1 = np.meshgrid(x, y)
z = img_gray.reshape(-1)

# %%
from matplotlib import cm


# %%
fig = plt.figure(figsize=(15,15))#创建图片
subplot = fig.add_subplot(111, projection='3d')#确定函数图像位置，并标注绘制的是3D图（projection）
# Customize the z axis
subplot.set_xlim(0, img_gray.shape[0])
subplot.set_ylim(0, img_gray.shape[1])
subplot.set_zlim(256, 0)
# sca = subplot.scatter(x1,y1, img_gray)
# bar = subplot.bar(x1, y1, img_gray)
srf = subplot.plot_surface(x1,y1,img_gray, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.show()


