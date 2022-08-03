# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 00:32:33 2021

@author: hp
"""

import  requests
import  re
import  time

def login():
    #创建session对象
    session = requests.session()
    
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    session.headers = headers
    
    #url1---请求登录页面，获得token
    url1 = 'https://github.com/login'
    response1 = session.get(url1)
    s1 = re.findall(r'\"authenticity_token\".+?\=\=\"', response1.text)
    s12 = re.findall(r'value.+?\=\=', s1[0])
    authenticity_token = s12[0][7:]
    print(s12[0][7:])
    
    timestamp = re.findall('name="timestamp" value="(.*?)"', response1.text)[0]
    print(timestamp)
    
    timestamp_secret = re.findall('name="timestamp_secret" value="(.*?)"', response1.text)[0]
    print(timestamp_secret)
    
    #url2---构建表单，进行登录请求
    url2 = 'https://github.com/session'
    data = {
        'commit': 'Sign in',
        'authenticity_token': authenticity_token,
        'login': 'chenzhaoqiJM',
        'password': '182842462206722377',
        'webauthn-support': 'supported',
        'webauthn-iuvpaa-support': 'unsupported',
        'return_to': 'https://github.com/login',
        'timestamp': timestamp,
        'timestamp_secret': timestamp_secret
    }
    response2 = session.post(url2, data=data)
    
    #url3---验证登录
    url3 = 'https://github.com/chenzhaoqiJM'
    response3 = session.get(url3)
    with open('github-zq.html', 'wb') as f:
        f.write(response3.content)
    
    
if __name__ == '__main__':
    login()