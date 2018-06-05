#/usr/bin/python3
#-*-coding:UTF-8-*-

import re

content='Hello 123456 World_This is a Regex Demo'

result=re.match('^Hello\s(\d+)\sWorld',content)

print(result)
print('')
print(result.group())
print('')
print(result.group(1))
print(result.span())

#提取字符串中的某一部分内容，将那部分内容用正则表达式表达并用()括起来
#用group(1)调用获取匹配的结果
