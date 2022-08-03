
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


#获取网页的url链接的内容
def getHTMLText(url):
    try:
        r = requests.get(url, headers=my_headers.get_baidu_0())
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
        
    except :
        print('爬取错误！！！')
        return ''
    
def fillUrlList(urlList, html):
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find_all('div', 'imgpage')
    
    
    for imgpage in tag:
        lilist = imgpage.find_all('li')
        for li in lilist:
            try:
                urlList.append(li['data-objurl']) 
            except:
                pass   
    




if __name__ == '__main__':
    url_0 = 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%8F%A4%E5%8A%9B%E5%A8%9C%E6%89%8E'
    
    # html = getHTMLText(url_0) #获取html
    # print(type(html))

    # obj_list = re.findall(r'\"objURL\"\:\".*?\"', html)
    # print(obj_list)
    # soup = BeautifulSoup(html, 'html.parser')
    # tag = soup.find_all('div', 'imgpage')
    # print(len(tag))
    
    #使用谷歌浏览器-忽略usb警告  忽略无用的日志
    # options=webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    # browser = webdriver.Chrome(chrome_options=options)

    #使用火狐浏览器
    browser = webdriver.Firefox()
    
    browser.get(url_0)
    
    count = 50
    for i in range(count):
        js = 'var q=document.documentElement.scrollTop=1000000'
        browser.execute_script(js)
        time.sleep(3) 
    
    html = browser.page_source
    with open('lazha.html', 'wb') as f:
        f.write(html.encode('utf-8'))
        
    browser.quit()
    
    
    #因为要登录，暂时使用浏览器上下载的html文件
    # file = open('C:\\Users\\hp\\Desktop\\雷姆_百度图片搜索.html', 'rb')
    # html = file.read()
    # file.close()
    
    # soup = BeautifulSoup(html, 'html.parser')
    
    # tag = soup.find_all('div', 'imgpage')
    # print(len(tag))
    
    
    
    
    urlList = []
    fillUrlList(urlList, html)
    
    count_name = 1
    for ur in urlList:
        name = count_name
        my_downloader.download_single_img(ur, headers=my_headers.get_baidu_0(), save_path='./baidu_lazha', file_name=str(name)+'.jpg' )
        count_name += 1
        
    
    








