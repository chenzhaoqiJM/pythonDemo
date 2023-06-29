import os
import cv2
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

front = cv2.imread(r'C:\Users\hp\Desktop\1.tiff', 2)
front = cv2.resize(front,[256,256])

fig = plt.figure(figsize=(20,20))
ax = Axes3D(fig)

X = np.arange(0, 1024, 4)
Y = np.arange(0, 1024, 4)
X, Y = np.meshgrid(X, Y)
Z = front
# Z[front>0] = 0
surf = ax.plot_surface(X, Y, Z, cmap='hot',
                       linewidth=0, antialiased=False)

# X = X.ravel()
# Y = Y.ravel()
# Z = Z.ravel()

# ax.set_xlim(0, 1024)
# ax.set_ylim(0, 1024)
# val = 1024*1024
# interv = 32
# ax.scatter(X[:val:interv], Y[:val:interv], Z[:val:interv], marker=',',linewidths=0.2)

plt.show()