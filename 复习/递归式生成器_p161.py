#!/usr/bin/python3
#-*-coding:UTF-8-*-


#先遍历所有的子列表,再调用flatten,使用另一个for循环生成展开的子列表中的所有元素
#只适用于序列,不适用于字符串
def flatten(nested):

    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element

    except TypeError:
        yield nested

print(list(flatten([[[1],2],3,4,[5,[6,7]],8])))
