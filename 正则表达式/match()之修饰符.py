#/usr/bin/python3
#-*-coding:UTF-8-*-

import re

content='''Hello 1234567 World_This
is a Regex Demo'''

result=re.match('^Hello.*?(\d+).*?Demo$',content,re.S)

print('result.group(1):',result.group(1))
print('result:group():',result.group())


#re.S:作用是使.匹配包括换行符所在内的所有字符
#re.I:使匹配对大小写不敏感
#re.L:做本地化识别(locale-aware)匹配
#re.M:多行匹配,影响^和$
#re.U:根据Unicode字符集解析字符,影响\w,\W,\b,\B
#re.X
