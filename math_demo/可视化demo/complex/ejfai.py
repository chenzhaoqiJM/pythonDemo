import matplotlib.pyplot as plt
import numpy as np

ax = np.linspace(0,np.math.pi*2*2,100)
aj = np.linspace(0,np.math.pi*2*2,100)

x = np.cos(ax)
y = np.sin(ax)

fig,axs = plt.subplots(2,1)

axs[0].plot(x,y)
axs[0].grid()
axs[0].set_aspect(1)



plt.legend()
plt.show()