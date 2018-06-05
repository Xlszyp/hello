#!/usr/bin/python3
#-*-coding:UTF-8-*-

class TestIterator(object):

    value=0

    def __next__(self):
        self.value+=1

        if self.value>10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self

ti=TestIterator()
print(list(ti))

print('\n')

class Test(object):

    def __init__(self):
        self.sum=0

    def __iter__(self):
        return self

    def __next__(self):
            
        self.sum+=1
        if self.sum>50:
            raise StopIteration
        return self.sum

te=Test()
print(list(te))

print('\n')

def Sum(n):
    sums=0
    for i in range(n):
        sums+=i
        print('10之间相加的和:',sums)

Sum(10)
