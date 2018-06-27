#!/usr/bin/python3
#-*-coding:UTF-8-*-

import socket,select

s=socket.socket()

#获取当前机器主机名
host=socket.gethostname()
port=1234
#服务器套接字
s.bind((host,port))
#监听地址
s.listen(5)
inputs=[s]

while True:
    rs,ws,es=select.select(inputs,[],[])
    for r in rs:
        if r is s:
            #接受客户端连接
            c,addr=s.accept()
            print('Got connection from',addr)
            inputs.append(c)
    else:
        try:
            #接收数据
            data=r.recv(1024)
            disconnected=not data
        except socket.error:
            disconnected=True

        if disconnected:
            #访问客户端套接字
            print(r.getpeername(),'disconnected')
            inputs.remove(r)
        else:
            print(data)
