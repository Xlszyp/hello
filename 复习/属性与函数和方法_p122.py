#!/usr/bin/python3
#-*-coding:UTF-8-*-

class Bird(object):

    song='Squaawk'

    def sing(self):
        print('Hello,world')

bird=Bird()
bird.sing()

#关联函数
birdsong=bird.sing
birdsong()
