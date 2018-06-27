#!/usr/bin/python3
#-*-coding:UTF-8-*-

from subprocess import Popen,PIPE

text=open('E:\我也不知道这是什么\z\网络编程\web编程\file.html').read()
tidy=Popen('tidy',stdin=PIPE,stdout=PIPE,stderr=PIPE)

tidy.stdin.write(text.encode())
tidy.stdin.close()

print(tidy.stdout.read().decode())