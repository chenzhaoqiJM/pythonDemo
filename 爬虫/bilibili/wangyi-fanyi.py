# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 00:32:33 2021

@author: hp
"""

import requests
import re
import json
import time
import random

url1 = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

hearders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    # ,
    # 'Cookie': 'BAIDU_SSP_lcr=https://www.baidu.com/link?url=-LTwy-kdnyKyOlO3_0gONxPhDLRQc0lr-BHQlFTt75K&wd=&eqid=fc402b060000ecf300000006611a38ef'
}


session = requests.session()
session.headers = hearders

url3 = 'https://fanyi.youdao.com/'
response3 = session.get(url3)
print(response3)

lts = str(int(time.time()*1000))
salt = lts + str(random.randint(1,9))
data1 = {
    'i': '字典',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': 'cb337cd7a9ae73adc95b5da7ccd23be0',
    'lts': lts,
    'bv': 'eda468fc64295ecf2810ab8a672c2db1',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
print(data1,'\n')
# data1['i'] = 'Created on Wed Jul  7 00:32:33 2021'


#中文转英文
response = session.post(url1, data=data1)

print(response.content.decode('utf-8'))

#利用json解析字典
# dict_data = json.loads(response.content)
# print(dict_data['translateResult'][0][0]['tgt'])