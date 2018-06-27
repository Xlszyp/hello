#!/usr/bin/python3
#-*-coding:UTF-8-*-

import random
from pprint import pprint

values=list(range(1,11))+'J Q K'.split()
suits='张三 李四 赵五 小六'.split()
deck=['{} of {}'.format(v,s) for v in values for s in suits]




random.shuffle(deck)
pprint(deck[:12])
