#!/usr/bin/python3
#-*-coding:UTF-8-*-

#当调用eat方法时,鸟类饿了进食,饱了则不饿了,返回else语句
class Bird(object):

    def __init__(self):
        self.hungry=True

    def eat(self):

        if self.hungry==True:
            print('eating......')
            self.hungry=False

        else:
            print('吃饱了,No,thanks')

b=Bird()
#print(b.hungry)
b.eat()
b.eat()


class SongBird(Bird):

    def __init__(self):
        self.sound='Squawk!叫声.'

    def sing(self):
        print(self.sound)


sb=SongBird()
print(sb.sound)

sb.sing()
