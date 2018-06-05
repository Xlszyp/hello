#!/usr/bin/python3
#-*-coding:UTF-8-*-

def Fib(n):
    if n<=1:
        return n
    else:
        return(Fib(n-1)+Fib(n-2))


nterms=int(input('您要输出几项?'))

if nterms<=0:
    print('请输入正数')
else:
    print('斐波那契数列:')
    for i in range(nterms):
        print(Fib(i))


#根据递归函数Fib(3)=Fib(2)+Fib(1)
#Fib(2)=1,Fib(1)=1,即Fib(3)=2
