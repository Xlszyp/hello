#!/usr/bin/python3
#-*-coding:UTF-8-*-

#手动包装法
class Myclass(object):
    #静态方法
    def smeth():
        print('This is a static method')
    smeth=staticmethod(smeth)

    #类方法
    def cmeth(cls):
        print('This is a class method of',cls)
    cmeth=classmethod(cmeth)

Myclass.smeth()
Myclass.cmeth()

print('\n')

#装饰器实现
class Myclass1(object):

    @staticmethod
    def smeth1():
        print('这是一个静态方法！')

    @classmethod
    def cmeth1(cls):
        print('这是一个类方法!',cls)

Myclass1.smeth1()
Myclass1.cmeth1()
