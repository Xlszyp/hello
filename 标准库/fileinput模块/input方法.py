#!/usr/bin/python3
#-*-coding:UTF-8-*-

#利用input方法读取遍历文件的所有行
import fileinput

for line in fileinput.input('1.txt'):
    print(line)
