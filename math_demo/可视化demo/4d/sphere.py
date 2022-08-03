from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, patches
from matplotlib import colors
from matplotlib.ticker import FormatStrFormatter, FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection, PatchCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

X = np.linspace(0., 1, 30) 
Y = np.linspace(0., 1, 30)  
Z = np.linspace(0., 1, 30) 

#生成球面
u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:30j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
print(u.shape)
# print(X)

X1,Y1 = np.meshgrid(X,Y)
squa_z = 1.0 - (X1-0.5)**2 + (Y1-0.5)**2
print('##sz: ', np.min(squa_z.reshape(-1,1)), np.max(squa_z.reshape(-1,1)))
Z1 = np.sqrt(1 - (X1-0.5)**2 + (Y1-0.5)**2) + 0.5

V = -np.exp(-X1**2) + Y1**2

# sh = X1.shape
# patches = np.concatenate(X1.reshape(sh[0],sh[1],1),Y1.reshape(sh[0],sh[1],1),Z1.reshape(sh[0],sh[1],1), axis=2)
# p = PatchCollection(patches, cmap=cm.jet, alpha=0.4)
# p.set_array(V.reshape(sh[0],sh[1],1))


fig = plt.figure()#创建图片
sub = fig.add_subplot(111, projection='3d')#确定函数图像位置，并标注绘制的是3D图（projection）

# sub.add_collection(p)
# plt.colorbar(p)

# V = V.reshape(-1)
# X1 = X1.reshape(-1)
# Y1 = Y1.reshape(-1)
# Z1 = Z1.reshape(-1)

# sca = sub.scatter(X1,Y1,Z1, c=V, cmap=cm.coolwarm, norm=colors.Normalize())
# fig.colorbar(sca, shrink=0.5, aspect=5)
print()

#颜色映射
V1 = np.reshape(V, (-1,1))
print(np.min(V1),np.max(V1))

norm_sum = np.abs(np.max(V1)) + np.abs(np.min(V1))
norm_d = np.min(V1)

V1 = (V1-norm_d)/norm_sum 
print(np.min(V1),np.max(V1))

cmap = cm.get_cmap('rainbow')
# for id, item in enumerate(V1):
#     colors_[id] = cmap(item)
# colors_ = colors_.reshape(4,-1)
V1 = np.reshape(V1, V.shape)
colors_ = cmap(V1)
print(colors_.shape)

#绘制曲面
# sur = sub.plot_surface(X1,Y1,Z1 ,cmap = cmap,facecolors=colors_)
sur = sub.plot_surface(x,y,z ,cmap = cmap,facecolors=colors_)
cb1 = fig.colorbar(sur, shrink=0.5, aspect=5)


def func(x, pos):
    return str(float(x)*norm_sum+norm_d)[0:4]
myformatter = FuncFormatter(func)
cb1.formatter = myformatter
cb1.update_ticks()
# cb1.ax.formatter = myformatter


# sur = sub.plot_surface(X1,Y1,Z1 ,cmap = cmap)
# fig.colorbar(sur, shrink=0.5, aspect=5)

sub.set_xlabel('$x$',fontsize=15)
sub.set_ylabel('$y$',fontsize=15)
sub.set_zlabel('$z$',fontsize=15)

# colormap = cm.gist_rainbow #更多颜色参考：https://matplotlib.org/2.0.2/users/colormaps.html

# sub.set_zlim(-1.01, 1.01)
# sub.zaxis.set_major_locator(LinearLocator(10))
# sub.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.show()