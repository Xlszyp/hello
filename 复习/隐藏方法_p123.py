#!/usr/bin/python3
#-*-coding:UTF-8-*-

#类中的方法调用私有隐藏方法

class Secretive:

    def __inaccessible(self):
        print('Bet you can see me..')

    def accessible(self):
        print('The secret message is:')
        self.__inaccessible()


s=Secretive()

s.accessible()
