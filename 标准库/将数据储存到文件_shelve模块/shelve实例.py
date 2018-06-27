#!/usr/bin/python3
#-*-coding:UTF-8-*-

import shelve

s=shelve.open('test.dat')

s['x']=['a','b','c']
temp=s['x']
temp.append('d')

s['x']=temp
print(s['x'])
