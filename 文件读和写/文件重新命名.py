#!/usr/bin/python3
#-*-coding:UTF-8-*-

import os




open('E:/我也不知道这是什么/z/文件读和写/test.txt','w')
os.rename('test2.txt','test1.txt')
print('文件重新命名成功！')

#重新命名文件名的时候需要open的路径为这个代码所保存的路径下
#或者是将重新命名文件名的代码保存在需要更改文件的路径下
#否则会报系统找不到指定文件的错误
