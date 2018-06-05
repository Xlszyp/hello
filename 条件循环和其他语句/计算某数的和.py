#!/usr/bin/python3
#-*-coding:UTF-8-*-

sum=0
n=int(input('请输入一个数字:'))
for i in range(n):
    sum+=i
    if sum>5049:
        print(sum)


