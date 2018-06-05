#/usr/bin/python3
#-*-coding:UTF-8-*-


#类循环，列出1至50的数字
class Fib(object):
    def __init__(self):
        self.a=0

    def __iter__(self):
        return self

    def __next__(self):
        self.a=self.a+1
        if self.a>50:
            raise StopIteration()

        return self.a

    def __getitem__(self,n):
        for x in range(n):
            a=n

        return a

for i in Fib():
    print(i)

#在交互模式中输出   >>>fib=Fib()
#                   >>>fib[6]
#则会输出类循环中的第6个元素值是多少
