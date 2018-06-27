#!/usr/bin/python3
#-*-coding:UTF-8-*-

from socketserver import TCPServer,StreamRequestHandler

class Handler(StreamRequestHandler):

    def Handle(self):
        #访问客户端套接字
        addr=self.request.getpeername()
        print('Got connection from',addr)
        #写入
        self.wfile.write('Thank you for connecting')
#''表示运行该服务器的计算机
server=TCPServer(('',1234),Handler)
server.serve_forever()
