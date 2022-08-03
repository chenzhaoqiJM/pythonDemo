# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 00:32:33 2021

@author: hp
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re

import sys
sys.path.append('E:\\python-demo\\爬虫\\')
from cHeaders import HeadersStore
from cWrapper import SingleFileDownloads

import time

my_headers = HeadersStore()
my_downloader = SingleFileDownloads()

url = 'https://www.bilibili.com/video/BV1Hb4y167c9?p=19'

#输入cookies
temp =  "_uuid=D1CAA31F-4E57-7486-814B-69A952A3505480010infoc; buvid3=864C7752-54AC-4B9A-A068-9BE5FA054BCA13436infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(u))umYY~~|0J'uYkl|JkJm~; fingerprint=309669c81a6dc77d1c431bbafe6f22c9; buvid_fp=864C7752-54AC-4B9A-A068-9BE5FA054BCA13436infoc; buvid_fp_plain=864C7752-54AC-4B9A-A068-9BE5FA054BCA13436infoc; SESSDATA=ddd53129%2C1642936527%2Cc4261%2A71; bili_jct=7a01469882ecd0e98068ab9c326505e3; DedeUserID=421148729; DedeUserID__ckMd5=5b4126326341dc5a; sid=ananf5dj; fingerprint3=96bb62b9000e3364f50337ae13c42e3a; fingerprint_s=6193f5bd7ea1c247008b339f46e172a8; bp_video_offset_421148729=556006077932333569; CURRENT_BLACKGAP=1; CURRENT_QUALITY=64"

cookie_list = temp.split('; ')

cookies = {}

for cookie in cookie_list:
    cookie_dict = cookie.split('=')
    cookies[cookie_dict[0]] = cookie_dict[-1]

# print(cookies)
#带cookies请求url
response = requests.get(url, headers = my_headers.get_simple())

#抽取响应的cookies
dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(dict_cookies)

#将字典的cookies转为cookies jar
jar_cookies = requests.utils.cookiejar_from_dict(dict_cookies)
print(jar_cookies)

#保存html文档
response.encoding = 'utf-8'
with open('bilibili-cookies-demo.html', 'wb') as f:
    f.write(response.content)