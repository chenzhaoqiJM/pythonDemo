
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


#百度网盘的下载链接
url = "https://xacu02.baidupcs.com/file/cb8eafc53g45b384847e15933ea640a5?bkt=en-660aa7a193f4106d4df05d7c4acd4533c1e6c401b0bf60aa0bb3ed9818e9911d4cc42d85bb471cfb1c603fb97a7fc39fbe20edde66cb608447a5f678a3a3b05b&fid=1496051507-250528-414141914293529&time=1627741090&sign=FDTAXUbGERLQlBHSKfWqi-DCb740ccc5511e5e8fedcff06b081203-HkfzbgegyIBeGFALv%2Bq%2BA1PnuDY%3D&to=129&size=2994608&sta_dx=2994608&sta_cs=12&sta_ft=zip&sta_ct=7&sta_mt=6&fm2=MH%2CXian%2CAnywhere%2C%2Chubei%2Ccnc&ctime=1594229153&mtime=1596677160&resv0=-1&resv1=0&resv2=rlim&resv3=5&resv4=2994608&vuk=1496051507&iv=0&htype=&randtype=&tkbind_id=0&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=en-2db5dedcf2ecf402ad444194af11112cad9633b13f51d577e3ed4654e2b2e356e8e9416bdcf22f6112c7c2ad85951bcdd9d5c27151c78b24305a5e1275657320&sl=76480590&expires=8h&rt=pr&r=369705433&vbdid=4101876345&fin=%E8%B5%9B%E9%81%93%E5%92%8C%E6%97%A0%E4%BA%BA%E8%BD%A6%E4%B8%89%E7%BB%B4%E6%A8%A1%E5%9E%8B%EF%BC%887%E6%9C%889%E6%97%A5%E6%9B%B4%E6%96%B0%EF%BC%89.zip&fn=%E8%B5%9B%E9%81%93%E5%92%8C%E6%97%A0%E4%BA%BA%E8%BD%A6%E4%B8%89%E7%BB%B4%E6%A8%A1%E5%9E%8B%EF%BC%887%E6%9C%889%E6%97%A5%E6%9B%B4%E6%96%B0%EF%BC%89.zip&rtype=1&dp-logid=303552350381291849&dp-callid=0.1&hps=1&tsl=80&csl=80&fsl=-1&csign=8tIisDGYcQ13LAP1WfuKAgA9R%2BQ%3D&so=0&ut=6&uter=4&serv=0&uc=760456734&ti=c77e04c9862927e5f5a58adfc13baca5ab141828f4032d1d305a5e1275657320&hflag=30&from_type=3&adg=c_cc29962de638b22fa2b8f467ddd5c2ad&reqlabel=250528_f_261d042eef4664ffd2781fa433d4c096_-1_ed440a3ed9239279a3d7d5982a4a5203&by=themis"

# './' ：下载到当前文件夹， 'ai.rar'：文件名，根据下载的文件名设置
# my_downloader.download_single_others(url, my_headers.get_baidu_0(), './', 'ac.zip', jindutiao=True)


#因为要登录，暂时使用浏览器上下载的html文件
# file = open('C:\\Users\\hp\\Desktop\\叶问4：完结篇：粤语版_电影_bilibili_哔哩哔哩.html', 'rb')
# html = file.read()
# soup = BeautifulSoup(html, 'html.parser')
# # print(soup.prettify()) #打印全部内容
# file.close()

# tag2 = soup.find_all('video')
# print(tag2, '\n')

# video_url = tag2[0]['src']
# print(video_url)
video_url = 'http://cn-hk-eq-bcache-03.bilivideo.com/upgcxcode/07/45/209584507/209584507_da8-1-192.mp4?e=ig8euxZM2rNcNbNV7WdVhwdlhbdBhwdVhoNvNC8BqJIzNbfqXBvEuENvNC8aNEVEtEvE9IMvXBvE2ENvNCImNEVEIj0Y2J_aug859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IMvNC8xNbLEkF6MuwLStj8fqJ0EkX1ftx7Sqr_aio8_&ua=tvproj&uipk=5&nbs=1&deadline=1628852725&gen=playurlv2&os=bcache&oi=391865670&trid=0000bc4c4c8dc8e14a0395207d30543d068dT&upsig=38cc2c77c38f5380e2b0ad93ee4225bb&uparams=e,ua,uipk,nbs,deadline,gen,os,oi,trid&cdnid=9597&mid=0&bvc=vod&nettype=0&orderid=0,2&logo=80000000'
my_downloader.download_single_others(video_url, my_headers.get_bilibili_0(), 'C:\\Users\\hp\\Desktop\\', '13.mp4', jindutiao=True)


# book_url = 'https://ebookimg.lorefree.com/assets/file/2019/07/18/083226/PyQt5%E5%BF%AB%E9%80%9F%E5%BC%80%E5%8F%91%E4%B8%8E%E5%AE%9E%E6%88%98%20-%20%E7%8E%8B%E7%A1%95%20&%20%E5%AD%99%E6%B4%8B%E6%B4%8B.epub'

# my_downloader.download_single_others(book_url, my_headers.get_baidu_0(), 'C:\\Users\\hp\\Desktop\\', '1.epub', jindutiao=True)




# zw_url = 'http://61.175.198.136:8083/rwt/288/http/GEZC6MJZFZZUPLSSG63B/kcms/download.aspx?filename=maJpWZD5WeWtiQxo2a0hjTrBVaCBTQl1mdoxEZNNGT35EZ4UEdPd3drN2Uh5GZOxUMxgXdTd2VCpVS=0TWxRGZ4JDVEhHVlNGNL9UYud1aiNESotEW5QnZZhTZxdXb2gVYsl3KLx2V3YFcvRGcaBnWXlWUKR&dflag=nhdown&tablename=CDFDLAST2017'
# my_downloader.download_single_others(zw_url, my_headers.get_baidu_0(), 'C:\\Users\\hp\\Desktop\\', '1.caj', jindutiao=True)

