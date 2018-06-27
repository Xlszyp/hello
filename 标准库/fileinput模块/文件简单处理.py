#!/usr/bin/python3
#-*-coding:UTF-8-*-

import sys
import fileinput

for line in fileinput.input(r'C:\Users\Administrator\Desktop\1111.txt'):
    sys.stdout.write('=>')
    sys.stdout.write(line)
