#!/usr/bin/python3
#-*-coding:UTF-8-*-

#p208

import fileinput, re

field_pat=re.compile(r'\[(.+?)\]')

#作用域字典,收集变量
scope={}

#用于调用re.sub
def replacement(match):
    code=match.group(1)
    try:
        #如果字段为表达式,就返回结果
        return str(eval(code,scope))
    except SyntaxError:
        return ''

#获取所有文本并合成一个新的字符串:

lines=[]
for line in fileinput.input():
    lines.append(line)
text=''.join(lines)


#替换所有与字段模式匹配的内容
print(field_pat.sub(replacement,text))

