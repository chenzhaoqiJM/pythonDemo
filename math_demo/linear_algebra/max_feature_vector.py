import cv2
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

if __name__ == '__main__':
    
    A = [[6,5] ,[1,2]]
    x0 = [[0], [1]]
    xk = x0
    uk = 0
    
    A = np.array(A, dtype=np.float64)
    x0 = np.array(x0, dtype=np.float64)
    
    
    #--------------绘图部分-------------------------
    fig = plt.figure(figsize=(30,30), dpi=100)
    ax = axisartist.Subplot(fig, 1,1,1)
    fig.add_axes(ax)
    
    ax.axis[:].set_visible(False)
    #
    ax.axis["x"] = ax.new_floating_axis(0, 0)
    ax.axis["y"] = ax.new_floating_axis(1, 0)
    #new_floating_axis(self, nth_coord, value, axis_direction='bottom')
    #新建可移动的坐标轴
    ax.axis["x"].set_axis_direction('top')
    ax.axis["y"].set_axis_direction('left')
    ax.axis["x"].set_axisline_style("->", size = 2.0)
    ax.axis["y"].set_axisline_style("->", size = 2.0)
    
    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.set_yticks([-2, -1, 1, 2])
    #设置刻度标识显示
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    
    plt.title('y = max_fv',fontsize = 14, pad = 20)
    
    # t = np.linspace(0, 2*np.pi)
    # y = np.sin(t)
    # ax.plot(t, y, color = 'red', linewidth = 2)
    ax.plot(np.linspace(-1.0, 1.0), np.linspace(1.0,1.0), color='blue', linewidth=1.0, linestyle='--')  # 虚线
    ax.plot(np.linspace(1.0, 1.0), np.linspace(-1.0,1.0), color='blue', linewidth=1.0, linestyle='--')  # 虚线
    ax.plot(np.linspace(-1.0, 1.0), np.linspace(-1.0,-1.0), color='blue', linewidth=1.0, linestyle='--')  # 虚线
    ax.plot(np.linspace(-1.0, -1.0), np.linspace(-1.0,1.0), color='blue', linewidth=1.0, linestyle='--')  # 虚线
    #
    plt.legend()
    plt.show()

    
    
    vector_val_list = []
    for i in range(0, 10):
        xk = A.dot(xk)
        vector_val_list = [item[0] for item in xk]
        uk = max(vector_val_list)
        print('xk:{}  uk:{}  xk+1:{}'.format(xk.reshape(-1), uk, (xk/uk).reshape(-1) ))
        print('\n')
        xk = xk/uk
        
    
    print(xk)
    print(uk)