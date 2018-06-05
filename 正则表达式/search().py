#/usr/bin/python3
#-*-coding:UTF-8-*-

import re

content='Extra stings Hello 1234567 World_This is Regex Demo Extra stings'

result=re.search('Hello.*?(\d+).*?Demo',content)

print(result)
print('')
print(result.group(1))

#match()方法是从字符串开头开始匹配，一旦开头不匹配则返回None，匹配即失败
#search()方法在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果，再返回匹配的内容
