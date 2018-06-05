#!/usr/bin/python3
#-*-coding:UTF-8-*-

file=open('E:/我也不知道这是什么/z/文件读和写/测试/shi.txt','w')

print(file.write('   春晓\n春眠不觉晓,\n处处闻啼鸟.\n夜来风雨声,\n花落知多少.'))

file=open('E:/我也不知道这是什么/z/文件读和写/测试/shi.txt','r')
print(file.read())

file.close()
