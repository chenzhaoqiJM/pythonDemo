# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 12:37:50 2021

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 10:16:35 2021

@author: zq
"""

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('my-xd.xls')

row_name = data.iloc[0]
row_name_list = []
for i in range(0, len(row_name)):
    row_name_list.append(row_name[i])
print(row_name_list)


#####给列重命名以方便使用
# data.rename(columns = \
#             {'附件':'序号', 'Unnamed: 1':'姓名', 'Unnamed: 2':'性别', 'Unnamed: 3':'准考证号', \
#              'Unnamed: 4':'毕业院校'}, inplace=True)
data.columns = row_name_list
data.drop([0], inplace=True) #丢弃无用行
print(data)




df = data['毕业院校'].value_counts(ascending = True)  #统计数量，返回series
# xb = data['性别'].value_counts(ascending = True)
print(df)

plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.figure(figsize=(15, 20), dpi=100) #设置画布的大小与分辨率
ax = plt.gca() #获取坐标轴，一共四个
ax.xaxis.set_ticks_position('top') #设置x轴到顶部

df.plot(kind = 'barh') #绘制直方图

# plt.figure(figsize=(7, 20), dpi=100) #设置画布的大小与分辨率
# ax = plt.gca()
# xb.plot(kind = 'bar')

# plt.show()

# data['毕业院校'].hist(bins=10)

# print(data)

# print(ser)