# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:47:41 2021

@author: hp
"""

import requests


from clint.textui import progress

#下载的数据链接
url1 = "https://mirrors.tuna.tsinghua.edu.cn/osdn/android-x86/71931/android-x86_64-9.0-rc2.iso"


r = requests.get(url1, stream=True)

with open("android-x86_64-9.0-rc2.iso", "wb") as f: #自动内存管理
    total_length = int(r.headers.get('content-length'))
    print(total_length)#打印数据的大小，以字节表示
    for ch in progress.bar(r.iter_content(chunk_size = 1024*1024), expected_size = (total_length/(1024*1024)) ):
        if ch:
            f.write(ch)