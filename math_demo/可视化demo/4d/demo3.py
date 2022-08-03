from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
from matplotlib.ticker import FormatStrFormatter, FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FixedLocator

X = np.linspace(0.25, 1,40) #α
Y = np.linspace(0.3*np.pi, 0.45*np.pi,40)  #θ
Z = np.linspace(0.05,0.15,40)  #β
print(X)

X,Y,Z = np.meshgrid(X,Y,Z)

print(X.shape)
a=np.sin(Y)
b=np.cos(Y)
V=(a+X)*((a-b)**2)*(1+4*(a-b)+4*(a-b)*(2.4+1.5*0.25)*(Z**2))/((b*b*(1+(2.4+1.5*0.25)*(Z**2))+(Z**2)*(a*a+X))*2*a)

# print(np.max(V, axis=2))
fig = plt.figure()#创建图片
sub = fig.add_subplot(111, projection='3d')#确定函数图像位置，并标注绘制的是3D图（projection）



V = V.reshape(-1)
# index = np.abs(V-1.0)<=0.001
index = np.logical_and(V<=2 , V>=1 )

V = V.reshape(-1)[index]
X = X.reshape(-1)[index]
Y = Y.reshape(-1)[index]
Z = Z.reshape(-1)[index]
print('######',np.sum(V<=20))
print(V.shape,np.min(V), np.max(V))
sca = sub.scatter(X,Y,Z, c=V,cmap=cm.coolwarm, norm=colors.Normalize())
fig.colorbar(sca, shrink=0.5, aspect=5)

ratio = 90.0/1.6
def func(x, pos):
    return str(float(x)*ratio)[0:4]
mylocator = FuncFormatter(func)
sub.yaxis.set_major_formatter(mylocator)

sub.set_xlabel('$x$',fontsize=15)
sub.set_ylabel('$y$',fontsize=15)
sub.set_zlabel('$z$',fontsize=15)

colormap = cm.gist_rainbow #更多颜色参考：https://matplotlib.org/2.0.2/users/colormaps.html

# sub.set_zlim(-1.01, 1.01)
# sub.zaxis.set_major_locator(LinearLocator(10))
# sub.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.show()