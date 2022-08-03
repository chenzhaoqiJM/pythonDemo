import requests
import re
from bs4 import BeautifulSoup

import numpy as np
import pandas as pd

import sys
sys.path.append('E:\\python-demo\\爬虫\\')
from cHeaders import HeadersStore
from cWrapper import SingleFileDownloads
my_headers = HeadersStore()
my_downloader = SingleFileDownloads()


#获取网页的url链接的内容
def getHTMLText(url):
    try:
        r = requests.get(url, headers=my_headers.get_project_1(), allow_redirects=False)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
        
    except :
        print('爬取错误！！！')
        return ''
    

#提取关键信息并 填充列表
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find('tbody')
    trs = tag.find_all('tr')
    
    for tr in trs:
        tds = tr.find_all('td')
        td0 = tds[0].string #排名
        tds = tds[-4:]
        u = [td0.strip(), tr.img['alt'].strip(), tds[-4].text.strip() , tds[-3].text.strip(), tds[-2].text.strip(), tds[-1].text.strip()] 
        # print(u, '\n\n\n')
        ulist.append(u)
    


    

#打印列表
def printUnivList(ulist):
    tplt = '{0:{6}^10}\t{1:{6}^10}\t{2:{6}^10}\t{3:{6}^10}\t{4:^10}\t{5:^10}'
    print(tplt.format('排名', '学校', '所在城市', '类型', '总分' , '办学层次', chr(12288)))
    for u in ulist:
        print(tplt.format(u[0], u[1], u[2], u[3], u[4] , u[5], chr(12288)) )

if __name__ == '__main__':
    # url = 'https://www.shanghairanking.cn/rankings/bcsr/2020'
    # html = getHTMLText(url)
    
    file = open('C:\\Users\\hp\\Desktop\\【软科排名】2021年最新软科中国大学排名_中国最好大学排名.html', 'rb')
    html = file.read()
    html = html.decode('utf-8')
    # print(soup.prettify()) #打印全部内容
    file.close()
    
    ulist = []
    fillUnivList(ulist, html)
    # print(ulist)
    
    # printUnivList(ulist)
   
  
    np_ulist = np.array(ulist)
    data = pd.DataFrame(np_ulist)
    print(data)
    # soup = BeautifulSoup(html, 'html.parser')
    # tag = soup.find('tbody')
    # trs = tag.find_all('tr')
    # # print(trs)
    # td0 = trs[0].find_all('td')[0].string
    # td0 = td0.strip()
    
    # print(td0)