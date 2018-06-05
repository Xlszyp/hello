#!/usr/bin/python3
#-*-coding:UTF-8-*-

girls=['alice','bernice','clarice']
boy=['chris','arnold','bob']


for g in girls:
    for b in boy:
        if g[0]==b[0]:
            print(g,'+',b)
