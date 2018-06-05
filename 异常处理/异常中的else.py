#/usr/bin/python3
#-*-coding:UTF-8-*-

def test(x,y):

    try:

        a=x/y
        print('a=',a)

    except:

        print('Error happened')

    else:

        print('It went as expected')

test(2,1)

#假如没有发生异常则会执行else字句
