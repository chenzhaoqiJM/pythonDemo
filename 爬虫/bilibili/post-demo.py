# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 00:32:33 2021

@author: hp
"""

import requests
import re
import json

url = 'http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=b87267b840dc7337'

url1 = 'http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=84c97b372263f356'

hearders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    # ,
    # 'Cookie': 'BAIDU_SSP_lcr=https://www.baidu.com/link?url=-LTwy-kdnyKyOlO3_0gONxPhDLRQc0lr-BHQlFTt75K&wd=&eqid=fc402b060000ecf300000006611a38ef'
}


data = {
    'from':'zh',
    'to':'en',
    'q':'山脉'
}
data1 = {
    'from':'en',
    'to':'zh',
}
data1['q'] = 'Created on Wed Jul  7 00:32:33 2021'

# response = requests.post(url, data=data)

#中文转英文
response = requests.post(url1, data=data1, headers= hearders)

print(response.content.decode('utf-8'))


#使用正则表达式---注意编码的问题text
#只能使用text产生的str对象
ch = re.findall(r'"out":"(.*?)"', response.content.decode())
s = ch[0]

print(s)
s = "\u521b\u5efa\u4e8e2021\u5e747\u67087\u65e5\u661f\u671f\u4e0900\uff1a32\uff1a33"
print(s)


#利用json解析字典
dict_data = json.loads(response.content)
print(dict_data['content']['out'])