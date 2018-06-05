#/usr/bin/python3
#-*-coding:UTF-8-*-

import re

content = 'Hello 123 4567 world_This is a Regex Demo'

print(len(content))


result=re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)

print(result)

print(result.group())

print(result.span())


#match()方法：向这个方法传入要匹配的字符串以及正则表达式，就可以检测这个正则表达式是否匹配字符串
