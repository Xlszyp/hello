#!/usr/bin/python3
#-*-coding:UTF-8-*-

import math

def test(a,b,c):
    y=b*b-4*a*c

    if a==0:
        if b==0:
            if c==0:
                return '方程根为全体实数'
            else:
                return '方程无根'
    else:
        if y<0:
            return '方程无根'
        else:
            x1=(-b+math.sqrt(y))/(2*a)
            x2=(-b-math.sqrt(y))/(2*a)
            return x1,x2
