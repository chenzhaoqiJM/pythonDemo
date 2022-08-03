# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:39:41 2021

@author: zq
"""

import urllib.request
#Python3.3后urllib2已经不能再用，只能用urllib.request来代替


url = 'https://gss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/'\
    'sign=89d2ca65a2014c08196e20a33a4b2e30/38dbb6fd5266d01669d2d9e49c2bd40734fa3536.jpg' 
    
f = urllib.request.urlopen(url) 
data = f.read() 
with open("demo.jpg", "wb") as code:     
    code.write(data)