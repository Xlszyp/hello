#/usr/bin/python3
#-*-coding:UTF-8-*-

class Student0(object):
    def __init__(self,names,scores):
        self.__names=names
        self.scores=scores

    def into(self):
        print('学生：%s\n分数：%d'%(self.__names,self.scores))
studt=Student0('Lisi',99)
studt.into()