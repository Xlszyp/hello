#!/usr/bin/python3
#-*-coding:UTF-8

num=100
print('函数调用前的num值:',num)

def test():
    
    global num  #使用global关键字将num变量变为局部变量
    num=200
    print('函数体中的num值：',num)


def func():
    print('函数体外的num值：',num)
