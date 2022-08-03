# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:39:41 2021

@author: hp
"""
import requests
from lxml import etree
import time
from cUrlDemo import MyLeran
 
'''
目标网站是一个图片网站
1.访问首页
2.定位到每个图片的下载链接
3.定位到每个图片对应的大图链接
4.下载，保存图片
'''
 
if __name__ == '__main__':
    my_spyder = MyLeran()
    
    my_spyder.url = 'http://www.netbian.com/meinv/'
    
    url_list = []
    for i in range(0, 100):
        if i == 0:
            url_list.append("http://www.netbian.com/meinv/index.htm")
        else:
            url_list.append("http://www.netbian.com/meinv/index_"+ str(i) + ".htm")
        
    for i in url_list:
        my_spyder.url = i;    
        my_spyder.get_one_page_imgs()
    