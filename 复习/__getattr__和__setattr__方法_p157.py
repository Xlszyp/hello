#!/usr/bin/python3
#-*-coding:UTF-8-*-

class Rectangle(object):

    def __init__(self):
        self.width=0
        self.height=0

    def __setattr__(self,name,value):
        if name=='size':
            self.width,self.height=value
        else:
            self.__dict__[name]=value

    def __getattr__(self,name):
        if name=='size':
            return self.width,self.height
        else:
            raise AttributeError()


r=Rectangle()
r.width=10
r.height=120
print(r.size)


r.size=15,100
print(r.width)
print(r.height)
