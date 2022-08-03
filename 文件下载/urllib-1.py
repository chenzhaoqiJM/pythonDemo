# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:39:41 2021

@author: hp
"""

import urllib.request 
import os
    
def ch(a, b, c):
    '''
    a: 已近下载的数据块
    b: 数据块的大小
    c: 文件的大小
    '''
    # print(b)
    # print(c)
    per = 100.0 * a * b/c 
    if per>100:
        per = 100 
        
    data_size_done = a*b / (1024.0)
    total_size = c / 1024.0
    # print(a*b)
    print("总大小为：{} Kb  已经下载了： {} Kb ".format(total_size, data_size_done))
    # print(" %.2f%%"%per )
    
url1 = "https://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fb-ssl.duitang.com%252Fuploads%252Fitem%252F201808%252F21%252F20180821114400_vapnl.jpg%26refer%3Dhttp%253A%252F%252Fb-ssl.duitang.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg%3Fsec%3D1630208913%26t%3D053d7d2def9636fb0896d3f5ca091c01&thumburl=https%3A%2F%2Fimg0.baidu.com%2Fit%2Fu%3D1220668820%2C4241881064%26fm%3D26%26fmt%3Dauto%26gp%3D0.jpg"

file_name = "leimu.jpg"
save_path = "./"
local_path = os.path.join(save_path, file_name)

#将url上面的内容释放到磁盘
#
urllib.request.urlretrieve(url1, local_path , reporthook=ch)