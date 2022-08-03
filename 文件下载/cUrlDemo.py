# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:39:41 2021

@author: hp
"""
import requests
from lxml import etree
import time
 
'''
目标网站是一个图片网站
1.访问首页
2.定位到每个图片的下载链接
3.定位到每个图片对应的大图链接
4.下载，保存图片
'''

class MyLeran():
    def __init__(self):
        self.url = url = 'http://www.netbian.com/meinv/'
        
    def get_one_page_imgs(self):
        t1 = time.time()
        # url = 'http://www.netbian.com/meinv/'
        url = self.url
        resp = requests.get(url)
        resp.encoding = 'gbk'
        with open('index.html', 'wb') as f:
            f.write(resp.content)
        tree = etree.HTML(resp.content)
    
        node_list = tree.xpath('/html/body/div[2]/div[2]/div[3]/ul/li')
    
        sub_url_list = []
        for node in node_list:
            if len(node.xpath('./a/@href')) > 0:
                sub_url = node.xpath('./a/@href')[0]
            if len(node.xpath('./a/@href')) > 0:
                title = node.xpath('./a/b/text()')[0]
                sub_url_list.append((sub_url, title))
        #
        base_url = 'http://www.netbian.com/'
        count = 0
        for sub_url, title in sub_url_list:
            s_page = base_url + sub_url
            s_resp = requests.get(s_page)
            s_tree = etree.HTML(s_resp.content)
            img = s_tree.xpath('/html/body/div[2]/div[2]/div[3]/div/p/a/img/@src')[0]
            suffix = img.split('.')[-1]
            img_resp = requests.get(img)
            with open(f'./image/{title}.{suffix}', 'wb') as f:
                img_content = img_resp.content
                f.write(img_content)
                f.close()
            s_resp.close()
            img_resp.close()
            print("完成第 "+ str(count) + "图片的下载！")
            count += 1
        t2 = time.time()
        print("完成一页的下载！！！！")
        print(t2-t1)