#/usr/bin/python3
#-*-coding:UTf-8-*-

class Sum(object):
    def __init__(self):
        self.a=0

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(101):
            self.a=self.a+i

        if self.a>5050:
            raise StopIteration()

        return self.a


for x in Sum():
    print(x)
            
