
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

def getHtmlUrl(url):
    try:
        r = requests.get(url, timeout=200)
        r.raise_for_status() #状态不对则产生异常
        r.encoding = r.apparent_encoding
        return r.text
    except :
        print("产生异常")
        return ""

#***************************
# r = 0;
# try:
#     #设置请求的headers
#     hd = my_headers.get_baidu_0()
#     # print(hd)
    
#     #设置代理服务器
#     pxs = {"http": "http://user:pass@10.10.10.1:1234", "https":"https://183.232.232.92:443"}
    
#     #设置访问的网址
#     url = 'https://www.baidu.com//s' #在搜索框搜索
#     url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C0%D7%C4%B7&fr=ala&ala=1&alatpl=normal&pos=0'
    
#     kv = {'wd': 'leimu'} #设置要在搜索框里面输入是值
    
#     r = requests.get(url, headers = hd)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
# except :
#     print("error !!!")
    
# print(r.text)
# print(r.request.headers )

#下载图片示例
# img_url = 'https://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fimg.mp.itc.cn%252Fupload%252F20161202%252F8f9e4d8731994f7a92e7bbbba93f9d87_th.jpeg%26refer%3Dhttp%253A%252F%252Fimg.mp.itc.cn%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg%3Fsec%3D1630303510%26t%3D06fac864413328a8ac184910935e19ee&thumburl=https%3A%2F%2Fimg0.baidu.com%2Fit%2Fu%3D1195961000%2C1430608903%26fm%3D26%26fmt%3Dauto%26gp%3D0.jpg'
# my_downloader.download_single_img(img_url,my_headers.get_baidu_0(), './', '')


#下载视频示例

# video_url = "https://mooc1vod.stu.126.net/nos/mp4/2017/03/07/1005930032_6ec7044b4d9044498a14f83c1f412aa6_sd.mp4?ak=7909bff134372bffca53cdc2c17adc27a4c38c6336120510aea1ae1790819de83e9b50b23fdd8d95069983bcc4c383e884f342d8c65aa2e2bc6555c691030b693059f726dc7bb86b92adbc3d5b34b1329725b9c703ba6d2c6296260e355335f64426afeac364f76a817da3b2623cd41e"
# my_downloader.download_single_video(video_url, my_headers.get_baidu_0(), './', '2-4-3.mp4')


#获取ip地址的归属地
# ip_url = 'https://www.ip138.com/iplookup.asp?ip='
# ip_url = ip_url + '112.111.121.133' + '&action=2'
# r = requests.get(ip_url, headers = my_headers.get_baidu_0())
# r.encoding = r.apparent_encoding
# print(r.text)
# print(r.status_code)



#bs4示例
# url = 'https://python123.io/ws/demo.html'
# r = requests.get(url, headers = my_headers.get_baidu_0())
# demo = r.text
# soup = BeautifulSoup(demo, 'html.parser')

file = open('1.html', 'rb')
html = file.read()
soup = BeautifulSoup(html, 'html.parser')

# print(demo)
#下行遍历----------------------------------------------
print(soup.head, '\n')
print(soup.head.attrs, '\n') #打印标签的属性或者是描述
print(soup.head.contents, '\n') #返回字节点的列表

print(soup.body.contents, '\n') #获得body标签的子节点，包括字符串

print('遍历子节点---------------')
for chird in soup.body.children:
    print(chird)
print('\n')

#上行遍历-----------------------------------------------
print('打印title的父标签')
print(soup.title.parent, '\n')
print('打印html的父标签')
print(soup.html.parent, '\n')


print('遍历a标签的父标签，注意使用的是迭代器')
for i in soup.a.parents:
    if i is None:
        print(i)
    else:
        print(i.name)
print('\n')
        
#平行遍历------------------------------------------------
print('平行遍历示例********************************************')
print('先打印a标签的父标签')
print(soup.a.parent, '\n')
print('打印a标签')
print(soup.a, '\n')
print('a的下一个平行标签')
print(soup.a.next_sibling, '\n')
print('a标签的下下个平行标签')
print(soup.a.next_sibling.next_sibling, '\n')
print('a标签的前一个平行节点')
print(soup.a.previous_sibling, '\n')
print('迭代器向后遍历')
for sib in soup.a.next_siblings:
    print(sib)
print('\n')

print('迭代器向前遍历')
for sib in soup.a.previous_siblings:
    print(sib)
print('\n')


#保存html文件的示例---------------------------------------------
print('打印加工后的html')
print(soup.prettify(), '\n')
# print(type(soup.prettify()), '\n')
# with open('./1.html', 'wb') as f:
#     f.write(soup.prettify().encode('utf-8'))
#     f.close()

print('打印所有a标签之下的href')
for link in soup.find_all('a'):
    print(link.get('href'))
print('\n')


# print('打印所有标签')
# print(soup.find_all(True))
# print('\n')

print('带属性查找')
print(soup.find_all('p', 'course'), '\n')
print(soup.find_all(id = 'link1'), '\n')
print(soup.find_all(id = re.compile('link')), '\n')

