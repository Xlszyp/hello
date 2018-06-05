#/usr/bin/python3
#-*-coding:UTF-8-*-

def test(x,y):

    try:

        a=x/y
        b=name

        print('a=',a,b)

    except (ZeroDivisionError,NameError,TypeError) as e:

        print(e)


test(2,0)

#except子句访问异常对象本身，将异常对象真正的错误信息返回，而不是返回自己定义的异常信息
