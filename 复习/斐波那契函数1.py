#!/usr/bin/python3
#-*-coding:UTF-8-*-

def fib(num):
    result=[0,1]

    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
