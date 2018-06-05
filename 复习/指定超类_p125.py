#!/usr/bin/python3
#-*-coding:UTF-8-*-

class Filter(object):

    def init(self):
        self.blocked=[]

    def filter(self,sequence):

        for x in sequence:
            if x not in self.blocked:
                print(x)
        
class SPAMFilter(Filter):

    def init(self):
        self.blocked=['SPAM']

f=Filter()
f.init()
f.filter([1,2,3,'SPAM'])    #第一个实例中self.blocked=[]为空值,所以不会过滤SPAM

print('\n')

#第二个类继承了第一个类所有的功能,并self.blocked=['SPAM'],所以有过滤功能
s=SPAMFilter()
s.init()
s.filter(['SPAM','xls','day','SPAM'])
