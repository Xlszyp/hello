#!/usr/bin/python3
#-*-coding:UTF-8-*-

def f():
    a=0
    b=1
    a,b=b,a+b
    return a

f(5)
