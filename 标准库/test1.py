#!/usr/bin/python3
#-*-coding:UTF-8-*-

a=['a','b','c','d','e','f']
b=['1','2','3']
l=[]
for x in b:
    for y in a:
        z=x+y
        print(z)
        l.append(z)
print(l)
