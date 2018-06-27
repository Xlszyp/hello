#!/usr/bin/python3
#-*-coding:UTF-8-*-

from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver

class SimpleLoogger(LineReceiver):

    def connectionMade(self):
        print('Got connection from',self.transport.client)

    def connectionLost(self,reason):
        print(self.transport.client,'disconnected')

    def lineReceived(self,line):
        print(line)

factory=Factory()
factory.protocol=SimpleLoogger

reactor.listenTCP(2345,factory)
reactor.run()