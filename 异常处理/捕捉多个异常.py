#/usr/bin/python3
#-*-coding:UTF-8-*-

def sum(x,y):

    try:    

        b=name
        a=x/y
        print('a=',a)
        

    except ZeroDivisionError:

        print('y不能为0')

    except NameError:

        print('sum函数中没有name元素')


sum(2,0)
