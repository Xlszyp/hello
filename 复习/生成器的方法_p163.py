#!/usr/bin/python3
#-*-coding:UTF-8-*-

def repeater(value):

    while True:
        new=(yield value)

        if new is not None:
            value=new

r=repeater(6)
print(r)
print(next(r))

print(r.send('Hello,world！'))
print(r.send(r))
