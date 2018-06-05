#!/usr/bin/python3
#-*-coding:UTF-8-*-

#没有重写
class A(object):

    def hello(self):
        print('hello,Im A.')

class B(A):
    pass

a=A()
a.hello()

b=B()
b.hello()


#重写方法
class X(object):

    def hi(self):
        print('hi,Im X!')

class Y(X):

    def hi(self):
        print('hi,Im Y!')


x=X()
x.hi()

y=Y()
y.hi()
