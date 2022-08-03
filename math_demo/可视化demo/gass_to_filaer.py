
import matplotlib.pyplot as plt
import math
import numpy as np
from math import pi

if __name__ == '__main__':
    
    thegma = 1.0
    miu = 0.0
    gass_t = np.linspace(-10.0, 10.0, num=1500, dtype=np.float32)
    e_factor = ((gass_t-miu)*(gass_t-miu)) * ( -1.0/(2.0*thegma*thegma) )
    print("##########", e_factor[749])
    gass_y = ( 1.0/(math.sqrt(2*math.pi)*thegma) ) * np.exp(e_factor)
    
    
    #在频率域取一个区间的离散频率值
    f = np.linspace(-10.0, 10.0, num=1500, dtype=np.float32)
    # print(u)
    #根据傅里叶变换公式求出每个频率对应的峰值
    limit_f = np.exp(-(f*f) * 2*math.pi*math.pi*thegma*thegma)
    # limit_f = limit_f/(limit_f.sum(axis=0)) / math.sqrt(2*pi)
    limit_f = limit_f*20.0/1500.0 #得到时域下的峰值
    # print(y_f)
    
    #在时间域上取一段区间用于作图
    t = np.linspace(-10.0, 10.0, num=1500, dtype=np.float32)
    
    #用cos(2pift)公式计算每个频率在给定时间段上的余弦值
    f_c = f.reshape(f.shape[0], 1 )
    t_c = t.reshape(1, t.shape[0])
    ft = f_c.dot(t_c)   #用频率乘以每一个时间离散向量
    y_ft = np.cos(2*math.pi*ft)
    
    limit_f = limit_f.reshape(limit_f.shape[0],1)
    limit_f_matrix = np.repeat(limit_f, limit_f.shape[0], axis=1)

    y_ft_limit = y_ft*limit_f_matrix #逐元素相乘
    y_ft_limit_sum = y_ft_limit.sum(axis=0) #第一维的向量全部加起来
    print(y_ft_limit.shape)
    
    err = y_ft_limit_sum-gass_y
    print("The L2 norm of err vector is: {}".format(np.linalg.norm(err, ord=2)))

    fig = plt.figure(figsize=(30,21), dpi=300) #生成画布
    # # 画线
    # plt.plot(t , y_ft_limit_sum,color="red",label="f line" ,linewidth=2) #画折线
    # plt.plot(gass_t , gass_y ,color="green",label="gass line" ,linewidth=0.5) #画折线
    # plt.xlabel("t", fontsize=18) #x轴标签
    # plt.ylabel("y", rotation='horizontal', fontsize=18) #y轴标签
    # plt.legend()
    # plt.show()
    
    
    ax = fig.add_subplot(1,1,1)
    plt.ion()
    plt.title("result")
    plt.xlabel("bo")
    plt.ylabel("add")
    plt.plot(gass_t , gass_y ,color="blue",label="gass line" ,linewidth=2, zorder=40) #画标准正态函数
    length = y_ft_limit.shape[0]
    add_result = y_ft_limit[length//2]
    #
    ans = ax.plot(t, y_ft_limit[length//2])
    plt.pause(0.2)
    for i in range(1, length//2):

        add_result = add_result + y_ft_limit[length//2+i] + y_ft_limit[length//2-i]
        # plt.cla()
        a = ax.plot(t, y_ft_limit[length//2+i], linewidth=4, zorder=10)
        plt.pause(0.2)
        b = ax.plot(t, y_ft_limit[length//2-i], linewidth=4, zorder=20)
        plt.pause(0.2)
        
        ax.lines.remove(a[0])
        ax.lines.remove(b[0])
        ax.lines.remove(ans[0])
        ans = ax.plot(t, add_result, linewidth=4, zorder=30)
        plt.pause(0.5)

        if i == 1:
            plt.pause(2)  # 启动时间，方便截屏
            


    plt.ioff()
    fig.tight_layout()
    plt.show()