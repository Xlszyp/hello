#!/usr/bin/python3
#-*-coding:UTF-8-*-

f=open('E:/我也不知道这是什么/z/文件读和写/测试/shi.txt','r',encoding='utf-8')
f_new=open('E:/我也不知道这是什么/z/文件读和写/测试/newshi.txt','w',encoding='utf-8')



        
line=f_new.write('   春晓\n春眠不觉晓,\n处处闻啼了.\n夜来风雨声,\n花落知多少.')
print(line)
f.close()
f_new.close()
