#/usr/bin/python3
#-*-coding:UTF-8-*-

import re

content='Hello 123 4567 World_This is a Regex Demo'

result=re.match('^Hello.*Demo$',content)

print(result)
print('')
print(result.group())
print('')
print(result.span())

#.*,.可以匹配任意字符（除换行符）,*代表匹配前面的字符无限次,所以.*组合一起就可以匹配任意字符
