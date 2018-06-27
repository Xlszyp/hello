#!/usr/bin/python3
#-*-coding:UTF-8-*-

import fileinput

def process(line):
    return line.rstrip()+' line'

for line in fileinput.input(['2.txt']):
    print(process(line))

'''
    如果要修改两个文件的内容：
        for line in fileinput.input(['2.txt',3.txt],inplace=1):
            print(process(line))
'''

        
