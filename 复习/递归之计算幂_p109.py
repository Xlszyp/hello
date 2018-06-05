#!/usr/bin/python3
#-*-coding:UTF-8-*-

def power(x,n):
    result=1
    for i in range(n):
        result*=x

    return result

print(power(2,3))


def power1(X,N):
    if N==0:
        return 1
    else:
        return X*power1(X,N-1)

print(power1(3,3))

#原理：已知X=3，powerv1(X,N-1)=9,所以3*9=27
