
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 00:32:33 2021

@author: hp
"""

import requests
from bs4 import BeautifulSoup
from cHeaders import HeadersStore
from cWrapper import SingleFileDownloads
import re

my_headers = HeadersStore()
my_downloader = SingleFileDownloads()

#因为要登录，暂时使用浏览器上下载的html文件
file = open('C:\\Users\\hp\\Desktop\\Python网络爬虫与信息提取_中国大学MOOC(慕课).html', 'rb')
html = file.read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify()) #打印全部内容
file.close()
tags = soup.find_all('video')
print(tags)

html = html.decode()

print(type(html))
# print(html)

match = re.search(r'<video.*video>', html)


if match:
    print(match.group(0))


match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0), '\n')
    
#使用match方法从头开始匹配
match2 = re.match(r'[1-9]\d{5}', '100081 BIT')
if match2:
    print(match2.group(0))
    
#使用findall方法发现所有的匹配
listM = re.findall(r'[1-9]\d{5}', 'BIT 100081 cs 618107')
print(listM, '\n')

#使用split函数在匹配完全之后完成分割
new_s = re.split(r'[1-9]\d{5}', 'BIT 100081 CS618107 WH610007')
print(new_s, '\n')

#返回迭代器的方式
for mc in re.finditer(r'[1-9]\d{5}', 'BIT 100081 CS618107 WH610007'):
    if mc:
        print(mc.group(0))
print('\n')

#z字符串替换
new_r_s = re.sub(r'[1-9]\d{5}', 'code',  'BIT 100081 CS618107 WH610007')
print(new_r_s, '\n')

#b
recp = re.compile(r'[1-9]\d{5}')
new_r_s = recp.sub('code',  'BIT 100081 CS618107 WH610007')
print(new_r_s, '\n')

mt3 = recp.search( 'BIT 100081 CS618107 WH610007')
print('.string:', mt3.string, '  ', '.re:', mt3.re, ' ', '.pos:',mt3.pos, ' ', '.endpos:',mt3.endpos, \
    '\n', '.group:', mt3.group(0), ' ', '.start:', mt3.start(), ' ', '.end', mt3.end(),\
        '\n', ' ', '.span:', mt3.span())





