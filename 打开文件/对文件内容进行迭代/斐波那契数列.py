#!/usr/bin/python3
#-*-coding:UTF-8-*-


def Fib(n):

    a=b=1
    for i in range(n):
        yield a
        
        a,b=b,a+b


for x in Fib(50):
    print(x)
