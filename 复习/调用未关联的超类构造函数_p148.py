#!/usr/bin/python3
#!-*-coding:UTF-8-*-

class Bird(object):

    def __init__(self):
        self.hungry=True

    def eat(self):

        if self.hungry==True:
            print('eating....')
            print('No hungry...')
            self.hungry=False
        else:
            print('No,thank!')



class SongBird(Bird):

    def __init__(self):
        #类调用方法,称为未关联的,用Bird类调用其中的方法
        Bird.__init__(self)
        
        self.sound='Aha!'
    def sing(self):
        print(self.sound)

sb=SongBird()
sb.sing()
sb.eat()
sb.eat()
