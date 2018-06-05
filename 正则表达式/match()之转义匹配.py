#/usr/bin/python3
#-*-coding:UTF-8-*-

import re

content='(百度)www.baidu.com'

result=re.match('^\(百度\)www.*?(\w+).*?com$',content)

print(result)

print(result.group(1))
print(result.group())
