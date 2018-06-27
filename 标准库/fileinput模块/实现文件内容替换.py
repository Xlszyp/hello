#!/usr/bin/python3
#-*-coding:UTF-8-*-

import fileinput

for line in fileinput.input('3.txt'):
    print(line.rstrip().replace('python','per1'))


'''
    实现原文件备份：
        for line in fileinput.input('data.txt',backup='.bak',inplace=1):  
            print line.rstrip().replace('Python','Perl')
'''
