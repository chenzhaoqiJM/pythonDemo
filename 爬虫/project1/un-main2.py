import requests
import re


def getHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("getHtmlText err")
    
def parsePage(ulist,html):
    try:
        ranking=re.findall(r'\"ranking\"\:\"[\d]*\"',html)
        univNameCn=re.findall(r'\"univNameCn\"\:\".*?\"',html)
        scores=re.findall(r'\"score\"\:[\d]*',html)
        
        for i in range(30):
            rank=eval(ranking[i].split(":")[1])
            name=eval(univNameCn[i].split(":")[1])
            score=eval(scores[i].split(":")[1])
            ulist.append([rank,name,score])
    except:
        print("parsePage err")
        
        
def printGoodsList(ulist):
    tplt = "{0:^10}{1:{3}^10}{2:^10}"
    print(tplt.format("序号", "学校名称", "分数", chr(12288)))  # 中文空格填充，能保证输出对齐
    for i in range(len(ulist)):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
        


def main():
    url = "https://www.shanghairanking.cn/api/pub/v1/bcur?bcur_type=11&year=2020"
    ulist = []
    html = getHtmlText(url)
    parsePage(ulist,html)
    printGoodsList(ulist)
main()