#!/usr/bin/python3
#-*-coding:UTF-8-*-

class CounterList(list):
    def __init__(self,*args):
        super().__init__(*args)
        self.count=0
        

    def __getitem__(self,index):
        self.count+=1
        return super(CounterList, self).__getitem__(index)


cl=CounterList(range(10))
print(cl)

print(cl[1]+cl[2])
n1=cl.count
print('列表访问次数{}次'.format(n1/2))

print(cl[0]+cl[1])
n2=cl.count
print('列表访问次数{}次'.format(n2/2))
