#!/usr/bin/python3
#-*-coding:UTF-8-*-

x=int(input('请输入一个数字:'))
def square(x):
    'Calculates the square of the number x.'
    return x*x

print('输入数字的平方值为:',square(x))
print('注释文档:'+square.__doc__)
    
