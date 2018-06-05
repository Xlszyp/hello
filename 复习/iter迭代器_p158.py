#!/usr/bin/python3
#-*-coding:UTF-8-*-

class Fibs(object):

    def __init__(self):
        self.a=0
        self.b=1

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a

    def __iter__(self):
        return self

fib=Fibs()

for f in fib:
    if f>1000:
        print('大于1000的第一个值：',f)
        break

it=iter([1,2,3,4,5,6])

try:
    
    while True:
        print(next(it))

except StopIteration:
    
    print('迭代已结束！迭代器没有更多的值.')

    
