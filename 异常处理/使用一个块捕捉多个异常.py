#/usr/bin/python3
#-*-coding:UTF-8-*-

def sum(x,y):

    try:

        b=name
        a=x/y
        print('a=',a,b)

    except (ZeroDivisionError,NameError,TypeError):

        print('one of ZeroDivisionError or NameError or TypeError happened')


sum(2,2)


#使用一个块捕捉多个类型异常，可以将它们（异常类型）作为元组列出
#当遇到的异常类型是元组中的任意一个，则都会走异常流程
