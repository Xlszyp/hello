#/usr/bin/python3
#-*-coding:UTF-8-*-

def test(x,y):

    try:

        aa=x/y

        print('a=',a)

        return a

    except Exception:   #假如以上代码没有错误则返回a的值，否则返回except下的输出

        print('以上程序发生异常')

test(2,2)
