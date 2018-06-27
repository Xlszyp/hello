#!/usr/bin/python3
#-*-coding:UTF-8-*-

from random import randrange

num=int(input('你要掷几个骰子?'))
sides=int(input('每个骰子有几个面?'))

sum=0
for i in range(num):
    sum+=randrange(sides)+1
    #print('你掷的点数:',sum)
print('你掷的点数总和:',sum)
