# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:39:41 2021

@author: hp
"""


import  urllib.request
import  requests
import  re #正则表达式
import ssl
from clint.textui import progress


def getJpg(html):
    # jpgList= re.findall(r'(img src="http.+?.jpg")([\s\S]*?)(.+?.alt=".+?.")',html)
    # jpgList= re.findall(r'http.+?.jpg',str(jpgList))
    # return jpgList

  # ------ 利用正则表达式匹配网页内容找到图片地址 ------
    reg = r'src="([.*\S]*\.jpg)"'
    imgre = re.compile(reg);
    imglist = re.findall(imgre, html)
    return imglist


def downLoad(jpgUrl,sTitle ):
    try: 
        urllib.request.urlretrieve(jpgUrl, './image/%s.jpg'  %sTitle)
    finally: 
        print('图片---%s----下载操作完成' % sTitle)
        
def downLoad2(jpgUrl,sTitle ):
    try: 
        r = requests.get(jpgUrl, stream=True)
        with open('./image/%s.jpg', "wb") as f: #自动内存管理
            total_length = int(r.headers.get('content-length'))
            # print(total_length)#打印数据的大小，以字节表示
            for ch in progress.bar(r.iter_content(chunk_size = 1024), expected_size = (total_length/(1024)) ):
                if ch:
                    f.write(ch)
        r.close()
    finally: 
        print('图片---%s----下载操作完成' % sTitle)
        
        
def get_list_html(list_source):
    result = ""
    count = 0
    for i in list_source:
        send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Language": "h-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",

        }
        res = requests.get(url, send_headers)
        res.encoding = 'utf-8'
        html = res.text
        result += html
        if count>=99:
            res.close()
        ++count
    return result
        
        
if __name__== '__main__':    
    url= "http://www.netbian.com/meinv/index_3.htm"
    url_list = []
    
    for i in range(0, 100):
        if i == 0:
            url_list.append("http://www.netbian.com/meinv/index.htm")
        else:
            url_list.append("http://www.netbian.com/meinv/index_"+ str(i) + ".htm")
    # req = urllib.request.Request(url)
    
    
    # req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")

    # res= urllib.request.urlopen(req) 
    # html = res.read()
    # html = html.decode("utf-8")
    
    
    
    #获取单个url指向网址的html，最终为字符串形式
    #使用requests模块
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Language": "h-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        # "Host": "imgstat.baidu.com",
        # "Referer": "https://image.baidu.com/",
        # "sec-ch-ua": "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
        
        }
    res = requests.get(url, send_headers)
    res.encoding = 'utf-8'
    html = res.text
    print(type(html))
    res.close()
    
    
    #获得批量的图片超链接
    html = get_list_html(url_list)
     
    
    # title=re.findall('<title>(.+)</title>',html)
    # print (title)
    
    #利用正则表达式提取图片的链接
    urlJpgs= getJpg(html)
    print(len(urlJpgs))
    n= 0     
                    
    for urlJpg in  urlJpgs:
        print(n,'--- url -->',urlJpg)
        
        downLoad2(urlJpg, str(n) )
        n= n+ 1

