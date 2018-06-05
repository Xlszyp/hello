#!/usr/bin/python3
#-*-coding:UTF-8-

def story(**kwds):
    return (kwds)

print(story(x='xls'))


def test(*kw):
    return kw

print(test('xls','fz',22))
