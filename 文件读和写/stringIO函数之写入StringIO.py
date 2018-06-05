#!/usr/bin/python3
#-*-coding:UTF-8-*-

from io import StringIO

#创建一个StringIO
io_val=StringIO()

#将文件写入StringIO
io_val.write('hello')
print('say:',io_val.getvalue())

#数据的读取除了通过文件，还可以在内存中进行
