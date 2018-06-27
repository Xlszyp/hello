#!/usr/bin/python3
#-*-coding:UTF-8-*-


#将一个列表压入堆中
from heapq import *
from random import shuffle

data=list(range(10))
shuffle(data)
heap=[]

for n in data:
    heappush(heap,n)
    #print(heap) 这个会迭代循环出所有结果
print(heap)


#添加元素到堆
heappush(heap,0.5)
print(heap)
