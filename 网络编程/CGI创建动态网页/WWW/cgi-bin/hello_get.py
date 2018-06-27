#!/usr/bin/python3
#-*-coding:UTF-8-*-

import cgi

#创建FieldStorage的实例化
form=cgi.FieldStorage()


#获取数据
site_name=form.getvalue('name')
site_url=form.getvalue('url')

print('Content-type:text/html')
print()
print('<html>')
print('<head>')
print('<meta charset=\'UTF-8\'>')

print('<title> CGI测试</title>')
print('</head>')
print('<body>')
print('<h2>%s网站: %s</h2>'%(site_name,site_url))
print('</body>')
print('</html>')


#如网站无法跳转,可能是网页编码问题
