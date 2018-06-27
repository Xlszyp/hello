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

#heapreplace
heapreplace(heap,0.5)
print('更改后:',heap)
