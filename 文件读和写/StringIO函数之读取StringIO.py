#!/usr/bin/python3
#-*-coding:UTF-8-*-

from io import StringIO

io_val=StringIO('Hello\n World!\n Welcome!')

while True:
    line=io_val.readline()

    if line=='':
        break

    print('line value:',line.strip())
