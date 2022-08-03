from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def contours_1():
    delta = 0.025
    x = np.arange(-3.0, 3.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X,Y = np.meshgrid(x,y)
    Z1 = np.exp(-X**2-Y**2)
    Z2 = np.exp(-(X-1)**2-(Y-1)**2)
    Z=(Z1-Z2)*2
    return X,Y,Z

def contours_2():
    delta = 0.025
    x = np.arange(-3.0, 3.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X,Y = np.meshgrid(x,y)
    Z1 = np.exp(-(X+1)**2-(Y+0.5)**2)
    Z2 = np.exp(-(X-1)**2-(Y-0.5)**2)
    Z=(Z1-Z2)*2
    return X,Y,Z


fig = plt.figure(figsize=(16,9)) #生成画布
subplot1 = fig.add_subplot(221)
subplot2 = fig.add_subplot(222)
subplot3 = fig.add_subplot(223, projection='3d')
subplot4 = fig.add_subplot(224, projection='3d')

#************************************************************#
#第一个函数
X_1,Y_1,Z_1 = contours_1()
CS_1 = subplot1.contour(X_1,Y_1,Z_1)
subplot1.clabel(CS_1, inline=1, fontsize=8)
subplot1.set_title("contours_1")
subplot1.set_xlabel("X"); subplot1.set_ylabel("Y")

#第一个函数在三维空间作图
subplot3.set_title("contours_1_3D")
subplot3.set_xlabel('X Axes')
subplot3.set_ylabel('Y Axes')
subplot3.set_zlabel('Z Axes')
surf = subplot3.plot_surface(X_1,Y_1,Z_1, cmap=cm.coolwarm)     #画曲面
# surf = subplot3.plot_wireframe(X_1,Y_1,Z_1, cmap=cm.coolwarm) #画网格线的曲面
fig.colorbar(surf, ax=subplot3, shrink=0.5, aspect=10)




#***********************************************************#
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
# CS_4 = subplot4.plot_surface(X_2,Y_2,Z_2, cmap=cm.coolwarm)
CS_4 = subplot4.contour(X_2,Y_2,Z_2)
subplot4.clabel(CS_4, inline=1, fontsize=8)


#*************************************************************
# plt.xlabel("X")
# plt.ylabel("Y")
plt.grid(True)


# plt.title("Simplest default with labels")
plt.tight_layout()
plt.show()
