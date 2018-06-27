#!/usr/bin/python3
#-*-coding:UTF-8-*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

text=urlopen('http://python.org/jobs').read()
#实例化BeautifulSoup类
soup=BeautifulSoup(text,'html.parser')

jobs=set()
#soup.body获取文档体,访问第一个section,h2调用返回的对象
#string是链接的文本内容
for job in soup.body.section('h2'):
    jobs.add('{}({})'.format(job.a.string,job.a['href']))

print('\n'.join(sorted(jobs,key=str.lower)))