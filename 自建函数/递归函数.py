#!/usr/bin/python3
#-*-coding:UTF-8

def test(n):
    if n==1:
        return 1
    return n*test(n-1)
