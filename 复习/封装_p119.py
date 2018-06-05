#!/usr/bin/python3
#-*-coding:UTF-8-*-

class Test(object):

    def set_name(self,name):
        self.name=name
        


    def get_name(self):
        return self.name
        

test=Test()
test.set_name('xls')

print('My name is:',test.get_name())
