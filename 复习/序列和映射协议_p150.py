#!/usr/bin/python3
#-*-coding:UTF-8-*-

def chenk_index(key):

    if not isinstance(key,int):raise TypeError
    if key<0:raise IndexError

class ArithmeticSequence(object):

    def __init__(self,start=0,step=1):
        self.start=start
        self.step=step
        self.changed={}

    def __getitem__(self,key):

        chenk_index(key)

        try:
            return self.changed[key]
        except KeyError:
            return self.start+key*self.step

    def __setitem__(self,key,value):

        chenk_index(key)
        self.changed[key]=value

s=ArithmeticSequence(1,2)
print(s[1])
print(s.changed)

s[1]=4
print(s[1])

print(s[6])

print(s.changed)
