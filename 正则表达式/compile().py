#/usr/bin/python3
#-*-coding:UTF-8-*-

import re

content1='2018-1-10 12:00'
content2='2017-2-11 13:05'
content3='2016-3-12 14:10'

pattern=re.compile('\d{2}:\d{2}')

result1=re.sub(pattern,'',content1)
result2=re.sub(pattern,'',content2)
result3=re.sub(pattern,'',content3)

print(result1,result2,result3)

#sub()方法的第一个参数是正则表达式，但是这里没有必要重复写三个同样的正则表达式
#所以可以借助于compile()函数将正则表达式编译成一个正则表达式对象，以便复用
