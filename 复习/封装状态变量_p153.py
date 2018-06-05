#!/usr/bin/python3
#-*-coding:UTF-8-*-

class Rectangle(object):

    def __init__(self):
        self.width=0
        self.height=0

    def set_size(self,size):
        self.width, self.height=size
        #size=self.width, self.height

    def get_size(self):
        return self.width,self.height


r=Rectangle()

r.width=10
r.height=5
print('get_size:',r.get_size())

r.set_size((100,150))
print('width:',r.width)
print('height:',r.height)


def test(x,y):
    a=x,y
    print(a)

test(1,2)
