

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 09:58:49 2021

@author: hp
"""
import socket
import threading
import time


class MyThread(threading.Thread):
    def __init__(self,socket, addr):
        super(MyThread,self).__init__()
        self.sock = socket
        self.addr = addr
    def run(self):
        print('Accept new connection from %s:%s...' % self.addr)
        while True:
            data = self.sock.recv(1024) #会产生阻塞
            time.sleep(0.5) #消抖
            rt = data.decode('utf-8')
            if not data or rt == 'exit':
                break
            if rt == "1":
                print("11111")
                
            if rt == "2":
                print("22222222222")
                
            if rt == "3":
                print("3333333333")
            print ('recv %s' % rt)
        # 第五步：关闭Socket
        self.sock.close()
        print('Connection from %s:%s closed.' % self.addr)

#专门用于发送的线程
class MyThreadRecv(threading.Thread):
    def __init__(self, ip, port):
        super(MyThreadRecv,self).__init__()
        # 第一步：创建一个基于IPv4和TCP协议的Socket
        self.sockSend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockSend.bind((ip, port))
        self.sockSend.listen(5)
    def run(self):
        sock, addr = self.sockSend.accept()
        print("发送者被连接成功")
        while True:
            sock.send(b'Hello,I am server!\n')
            pass
            
#主线程  
class myLight:
    def __init__(self) :
        # 第一步：创建一个基于IPv4和TCP协议的Socket
        iPAddress = '192.168.1.149'; port = 9999
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((iPAddress, port))
        # 第二步:监听连接
        self.sock.listen(5)
        print('Waiting for connection...')

        while True:
            # 第三步:接收一个新连接:
            sock, addr = self.sock.accept()
            # 创建新线程来处理TCP连接:
            t = MyThread(sock, addr)
            t.start()
            
            port = port -1
            t1 = MyThreadRecv(iPAddress, port)
            t1.start()
            
    
if __name__=="__main__":
    s = myLight()
   
