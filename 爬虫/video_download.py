
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 00:32:33 2021

@author: hp
"""

import requests
from bs4 import BeautifulSoup
from cHeaders import HeadersStore
from cWrapper import SingleFileDownloads

my_headers = HeadersStore()
my_downloader = SingleFileDownloads()

#因为要登录，暂时使用浏览器上下载的html文件
file = open('C:\\Users\\hp\\Desktop\\Python网络爬虫与信息提取_中国大学MOOC(慕课).html', 'rb')
html = file.read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify()) #打印全部内容
file.close()

tag2 = soup.find_all('video')
print(tag2, '\n')
print([i.attrs for i in tag2])

video_url = tag2[0].next_element['src']
print(video_url)

#下载视频示例
# my_downloader.download_single_video(video_url, my_headers.get_baidu_0(), 'E:\\视频\\爬虫\\', '3-7-1.mp4')


my_downloader.download_single_others(video_url, my_headers.get_baidu_0(), 'E:\\视频\\爬虫\\', '4-10-1.mp4', jindutiao=True)





