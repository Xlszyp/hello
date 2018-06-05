#/usr/bin/python3
#-*-coding:UTF-8-*-

def sum(x,y):

    try:

        a=x/y
        print('a=',a)

        return a

    except ZeroDivisionError:

        print('以上代码出现错误')
        #raise用来返回更加详细的报错
        raise
           

sum(2,0)
