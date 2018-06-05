#!/usr/bin/python3
#-*-coding:UTF-8-*-

import collections
import json

#用collections模块中的Counter方法计数txt文本中字符的出现次数
file=open('E:/我也不知道这是什么/z/文件读和写/测试/shi.txt','r')
f=file.read()
print(f)

obj=collections.Counter(f)
print(obj)


'''obj=dict(obj)
for k,v in obj.items():
    print(k,v)
    fout=open('E:/我也不知道这是什么/z/文件读和写/测试/test2.txt','w+', encoding='utf-8')
    fout.write(obj)
'''

#用JSON序列化将统计出来的结果导入到另外一个txt文本中
files=dict(obj)
with open('E:/我也不知道这是什么/z/文件读和写/测试/test2.txt','w') as f:
    json.dump(files,f)

#反序列化对导入的文件进行解码
with open('E:/我也不知道这是什么/z/文件读和写/测试/test2.txt','r') as i:
    files=json.load(i)

print('\n导入到文本中:',files)

print('\n')
#将files迭代,
for k,v in files.items():
    print(k,':',v,'次')
