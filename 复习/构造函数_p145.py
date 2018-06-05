#!/usr/bin/python3
#-*-coding:UTF-8-*-

#__init__构造函数可以在对象创建后直接调用
class FooBar(object):

    def __init__(self,value):
        self.name=value

f=FooBar('xls')
print(f.name)



class Foobar(object):

    def __init__(self,name):

        self.name=name

    def foo(self):
        return self.name


fo=Foobar('zyp')
print(fo.foo())
