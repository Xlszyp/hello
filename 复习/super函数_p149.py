#!/usr/bin/python3
#-*-coding:UTF-8-*-

class Bird(object):

    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry==True:
            print('eating...')
            print('stop eat,No hungry!')
            self.hungry=False
        else:
            print('No,thanks!')

class SongBird(Bird):
    def __init__(self):
        
        #调用Bird父类中的方法
        super().__init__()
        
        self.sound='Aha!'

    def sing(self):
        print(self.sound)


sb=SongBird()

sb.sing()
sb.eat()
sb.eat()
