#/usr/bin/python3
#-*-coding:UTF-8-*-

def test(x,y):

    try:

        a=x/y
        print('a=',a)

    except ZeroDivisionError as e:

        print(e)

    finally:

        print('No matter what happened,I will show in front of you')

test(2,0)
        
#try、except、else、finally可以组合使用，但是else在except后面，finally在except和else的后面
