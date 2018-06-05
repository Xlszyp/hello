#!/usr/bin/python3
#-*-coding:UTF-8-*-


def test():
    num=0
    num+=1
    return num

def test2():
    new_num=test()
#    return test2   #返回函数
    print(test())
