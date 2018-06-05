#!/usr/bin/python3
#-*-coding:UTF-8-*-

class Rectangle(object):

    def __inint__(self):
        self.width=0
        self.height=0

    def set_size(self,size):
        self.width,self.height=size

    def get_size(self):
        return self.width,self.height
    
    size=property(get_size, set_size)

r=Rectangle()

r.width=20
r.height=120
print('get_size:',r.size)

r.size=150,100
print('width:',r.width)
print('height:',r.height)
