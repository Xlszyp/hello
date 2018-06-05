#!/usr/bin/python3
#-*-coding:UTF-8-*-


#break跳出for循环字符串

a='hello'
for i in a:
    if i=='l':
        break
    print(i)


#break跳出while循环数字


num=10
while num>0:
    num-=1
    print(num)
    if num==8:
        break


