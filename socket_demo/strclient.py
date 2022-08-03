# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 09:58:49 2021

@author: hp
"""

import socket
# 初始化Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接目标的IP和端口
s.connect(('192.168.188.197', 80))
# 接收消息
print('-->>'+s.recv(1024).decode('utf-8'))
# 发送消息
s.send(b'LED ON')
print('-->>'+s.recv(1024).decode('utf-8'))
# 关闭Socket
s.close()