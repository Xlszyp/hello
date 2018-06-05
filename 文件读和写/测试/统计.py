#!/usr/bin/python3
#-*-coding:UTF-8-*-

f_name=open('E:/我也不知道这是什么/z/文件读和写/测试/shi.txt','r').read()

mylen=len(f_name)

line_num=f_name.count('\n')

words_num=len(f_name.split())

print('字符个数共:%s个\n行数:%s行\n一行的字数:%s个'%(mylen,line_num,words_num))


f_name=open('E:/我也不知道这是什么/z/文件读和写/测试/shi.txt','r')
while True:
    shi=f_name.read(1)
    if not shi:
        break

    print(shi)

f_name.close()
