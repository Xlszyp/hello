#!/usr/bin/python3
#-*-coding:UTF-8-*-

#计算器

class Calculator(object):

    def calculator(self,expression):
        self.value=eval(expression)


class Talker(object):

    def talk(self):
        print('Hi,my value is:',self.value)

class TalkingCalculator(Calculator,Talker):
    pass


tc=TalkingCalculator()

x=input('请出入你要计算的值:')
tc.calculator(x)
tc.talk()


#设置对象的属性,在tc实例中添加name方法,其方法赋值xls

setattr(tc,'name','xls')
print(tc.name)
