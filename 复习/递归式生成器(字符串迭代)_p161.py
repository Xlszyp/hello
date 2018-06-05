#!/usr/bin/python3
#-*-coding:UTF-8-*-

def flatten(nested):

    try:
        #不迭代类似于字符串的对象
        try:
            nested+''
        except TypeError:
            pass
        else:
            raise TypeError

        for sublist in nested:
             for element in flatten(sublist):
                yield element

    except TypeError:
        yield nested


print(list(flatten(['foo',['bar',['baz']]])))
            
            
