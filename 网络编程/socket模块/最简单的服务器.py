#!/usr/bin/python3
#-*-coding:UTF-8-*-

import socket

s=socket.socket()

#获取当前机器主机名
host=socket.gethostname()
port=1234
#服务器套接字
s.bind((host,port))

#监听地址
s.listen(5)

while True:
    #接受客户端连接
    c,addr=s.accept()
    print('Got connection from',addr)
    #发送数据
    c.send('Thank you for connecting')
    c.close()
