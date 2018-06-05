#/usr/bin/python3
#-*-coding:UTF-8-*-


#类循环：1到100

class Fib(object):
    def __init__(self):
        self.a=0    #初始化一个计数器a，a=0

    def __iter__(self):
        return self     #实例本身就是迭代对象，所以返回自己

    def __next__(self):
        self.a=self.a+1     #计算下一个值

        if self.a>100:      #退出循环的条件
            raise StopIteration()   #当self.a的值循环的值大于100则退出循环
        return self.a   #退出循环后返回self.a的下一个值

for n in Fib():
    print(n)
