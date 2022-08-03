from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import os

def contours_1():
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    X, Y = np.meshgrid(x, y)
    Z = np.add(-np.power(X, 3), np.power(Y, 2))
    return X,Y,Z

def contours_2():
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    X, Y = np.meshgrid(x, y)
    
    Z = np.add(-np.power(X, 4), np.power(Y, 4))
    return X,Y,Z


fig = plt.figure(figsize=(16,9)) #生成画布
subplot1 = fig.add_subplot(221)
subplot2 = fig.add_subplot(222)
subplot3 = fig.add_subplot(223, projection='3d')
subplot4 = fig.add_subplot(224, projection='3d')

#1111111************************************************************#
#第一个函数
subplot1.set_title("contours_1")
subplot1.set_xlabel("X"); subplot1.set_ylabel("Y")
X_1,Y_1,Z_1 = contours_1()
colormap = cm.gist_rainbow #更多颜色参考：https://matplotlib.org/2.0.2/users/colormaps.html
CS_1 = subplot1.contour(X_1,Y_1,Z_1, cmap = colormap)
subplot1.clabel(CS_1, inline=1, fontsize=8)
#fig.colorbar参数：shrink指定了色彩条与图形高度的比例，aspect指定了色彩条本身的长宽比。ax指定要在哪个图绘制彩色条
fig.colorbar(CS_1, ax=subplot1, shrink=0.5, aspect=10) 


#第一个函数在三维空间作图
subplot3.set_title("contours_1_3D")
subplot3.set_xlabel('X Axes')
subplot3.set_ylabel('Y Axes')
subplot3.set_zlabel('Z Axes')
surf = subplot3.plot_surface(X_1,Y_1,Z_1, cmap = colormap)     #画曲面
# surf = subplot3.plot_wireframe(X_1,Y_1,Z_1, cmap=cm.coolwarm) #画网格线的曲面
fig.colorbar(surf, ax=subplot3, shrink=0.5, aspect=10)
#11111111************************************************************#



#222222222***********************************************************#
#第二个函数
X_2,Y_2,Z_2 = contours_2()
CS_2 = subplot2.contour(X_2,Y_2,Z_2)
subplot2.clabel(CS_2, inline=1, fontsize=8)
subplot2.set_title("contours_2")
subplot2.set_xlabel("X"); subplot2.set_ylabel("Y")

#第二个函数在三维空间作
subplot4.set_title("contours_2_3D")
subplot4.set_xlabel('X Axes')
subplot4.set_ylabel('Y Axes')
subplot4.set_zlabel('Z Axes')

# subplot4.plot_wireframe(X_2,Y_2,Z_2, alpha=0.3)
ax = fig.gca(projection='3d')
ax.plot_wireframe(X_2,Y_2,Z_2, alpha=0.3)
# CS_4 = subplot4.plot_surface(X_2,Y_2,Z_2, cmap=cm.Accent)
CS_4 = subplot4.contour(X_2,Y_2,Z_2)
subplot4.clabel(CS_4, inline=1, fontsize=8)
#222222222*************************************************************


#保存一定数量是图片来生成动态图
# for angle in range(95, 180, 3):
#     subplot4.set_zlabel("Angle: " + str(angle))
#     subplot4.view_init(30, angle) #通过ax.view_init(30, angle)设置图形的视角
#     filename = os.path.join("./images", (str(angle) + ".png"))
#     plt.savefig(filename)
#     print("Save " + filename + " finish")

#*************************************************************


plt.grid(True)
plt.tight_layout()
plt.show()
