#!/usr/bin/python3
#-*-coding:UTF-8-*-

nested=[[1,2],[3,4],[5]]

def flatten(nested):

    for sublist in nested:
        for element in sublist:
            
            yield element

for num in flatten(nested):
    print(num)

print(list(flatten(nested)))
