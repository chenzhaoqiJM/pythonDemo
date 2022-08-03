# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 00:32:33 2021

@author: hp
"""


import  requests

url = 'http://www.baidu.com'
url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C0%D7%C4%B7&fr=ala&ala=1&alatpl=normal&pos=0'

proxies = {
    'http':'http://183.165.195.69:17431',
    'https':'https://183.165.195.69:17431'
}

response = requests.get(url, proxies=proxies)

print(response.text)