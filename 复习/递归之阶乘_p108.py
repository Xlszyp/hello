#!/usr/bin/python3
#-*-coding:UTF-8-*-

def factorial(n):
    result=n
    for i in range(1,10):
        result*=i
    return result

print(factorial(10))
