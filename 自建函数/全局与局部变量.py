#!/usr/bin/python3
#-*-coding:UTF-8

total=0


def sum(arg1,arg2):
    total=arg1+arg2
    print('局部变量total的值是：',total)



def test():
    print('全局变量total的值是：',total)
    return total


sum(1,2)
test()
