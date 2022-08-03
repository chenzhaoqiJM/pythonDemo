#CrowTaobaoPrice.py
import requests
import re

import sys
sys.path.append('E:\\python-demo\\爬虫\\')
from cHeaders import HeadersStore


my_headers= HeadersStore()


def getHTMLText(url):

    try:

        r=requests.get(url,timeout=30)

        r.raise_for_status()

        r.encoding=r.apparent_encoding

        return r.text

    except:

        return ""

def parsePage(ilt,html):

    try:

        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)

        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)

        for i in range(len(plt)):

            price=eval(plt[i].split(":")[1])

            title=eval(tlt[i].split(":")[1])

            ilt.append([price,title])

    except:

        print("")

def printGoodsList(ilt):

    tplt = "{:4}\t{:8}\t{:16}"

    print(tplt.format("序号","价格","商品名称"))

    count=0

    for g in ilt:

        count=count+1

        print(tplt.format(count,g[0],g[1]))

    print("")

def main():

    goods="眼镜"

    depth=2

    start_url="https://s.taobao.com/search?q="+goods

    infoList=[]

    for i in range(depth):

        try:

            url=start_url +"&s="+str(44*i)

           

            html=requests.get(url,headers= my_headers.get_simple())

            print(html.text)

            parsePage(infoList,html.text)

        except:

            continue

    printGoodsList(infoList)

main()