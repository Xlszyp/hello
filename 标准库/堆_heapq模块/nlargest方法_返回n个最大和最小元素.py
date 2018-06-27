#!/usr/bin/python3
#-*-coding:UTF-8-*-

from heapq import *
from random import shuffle

data=list(range(10))
shuffle(data)
heap=[]

for n in data:
    heappush(heap,n)
print('堆:',heap)


#返回n个最大的元素

print('2个最大的元素:',nlargest(2,heap))
print('2个最小的元素:',nsmallest(2,heap))
