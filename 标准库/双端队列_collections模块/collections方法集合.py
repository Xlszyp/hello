#!/usr/bin/python3
#-*-coding:UTF-8-*-

from collections import deque

q=deque(range(5))
print('双端队列:',q)

#在结尾添加元素
q.append(5)
print('添加5到结尾',q)

#在开头添加元素
q.appendleft(6)
print('添加6到开头',q)

#提取出结尾的元素
print('提取末尾元素:',q.pop())
print('末尾元素被提取后的队列:',q)

#提取开头的元素
print('提取左边元素:',q.popleft())
print('左边元素被提取后的队列:',q)

#rotate方法调整队列元素的位置
q.rotate(1)
print('队列中元素向前移1:',q)
q.rotate(-1)
print('队列中元素向后移1:',q)
