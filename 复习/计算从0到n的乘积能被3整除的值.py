#!/usr/bin/python3
#-*-coding:UTF-8-*-

n=int(input('请输入一个数字:'))
for i in range(n):
    i*=i
    if i%3==0:
        print(i)
