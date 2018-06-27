#!/usr/bin/python3
#-*-coding:UTF-8-*-

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class SimpleLogger(Protocol):
    #新连接到来,调用事件处理程序
    def connectionMade(self):
        print('Got connection from', self.transport.client)

    #连接中断时,调用connectionLost
    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')

    #接收客户端的数据
    def dataReceived(self, data):
        print(data)
#实例化Factory,设置属性protocol,使用协议与客户端通信
factory = Factory()
factory.protocol = SimpleLogger

#指定监听的端口
reactor.listenTCP(1234, factory)
#启动服务器
reactor.run()
#测试:telnet 127.0.0.1 1234