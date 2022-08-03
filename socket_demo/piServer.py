

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 09:58:49 2021

@author: hp
"""
import socket
import threading
import time



def dealClient(sock, addr):
# 第四步：接收传来的数据，并发送给对方数据
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Hello,I am server!\n')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        rt = data.decode('utf-8')
        if not data or rt == 'exit':
            break
        if rt == "1":
            print("第一灯切换")
        if rt == "2":
            print("第二灯切换")
        if rt == "3":
            print("风扇")
        print ('recv %s' % rt)
        sock.send(('Loop_Msg: %s!' % rt).encode('utf-8'))
        # 第五步：关闭Socket
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    
if __name__=="__main__":
    # 第一步：创建一个基于IPv4和TCP协议的Socket
    # Socket绑定的IP(127.0.0.1为本机IP)与端口
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.1.149', 9999))
    # 第二步:监听连接
    s.listen(5)
    print('Waiting for connection...')
    
    while True:
        # 第三步:接收一个新连接:
        sock, addr = s.accept()
        
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=dealClient, args=(sock, addr))
        t.start()