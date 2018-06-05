#/usr/bin/python3
#-*-coding:UTF-8-*-

def test(x,y):

    try:

        a=x/y
        print('a=',a)

    finally:

        print('No matter what happened,I will show in front of you')


test(2,0)

#trt/finally语句不论发生什么异常与否都将执行finally下面的代码
#假如try子句中发生错误，finally被执行后，最后仍然会抛出异常
