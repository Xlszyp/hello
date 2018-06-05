#!/usr/bin/python3
#-*-coding:UTF-8-*-


class Fib(object):

    def __getitem__(self,n):

        a=0

        for i in range(n):
            a+=1

        return a

f=Fib()

print(f[10])
print(f)



def test(y):
    q=0
    for x in range(y):
        q+=1

    return q

print(test(12))
