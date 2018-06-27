#!/usr/bin/python3
#-*-coding:UTF-8-*-

from heapq import *
from random import shuffle

data=list(range(10))
shuffle(data)
heap=[]

for n in data:
    heappush(heap,n)

print('原堆的值为:',heap)

#弹出最小元素
print('最小的值为:',heappop(heap))
print('弹出最小元素后的堆:',heap)

for i in range(len(heap)):
    print('弹出当前最小元素',heappop(heap))
    print('当前堆中的元素:',heap)
