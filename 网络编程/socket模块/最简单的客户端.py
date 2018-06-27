#!/usr/bin/python3
#-*-coding:UTF-8-*-

import socket

s=socket.socket()

#获取当前机器主机名
host=socket.gethostname()
port=1234

#客户端套接字连接服务端
s.connect((host,port))
#接收数据
print(s.recv(1024))
print('交互完成！')