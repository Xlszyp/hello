#!/usr/bin/python3
#-*-coding：UTF-8-*-



import cgi

#创建FieldStorage实例
form=cgi.FieldStorage()

#获取值name,设置默认值为world
name=form.getvalue('name')

print("""Content-type:text/html

<html>
    <head>
      <title>Greeting Page</title>
    </head>
    <body>
      <h1>Hello, %s!</h1>

      <form action='simple3.cgi'>
      Change name <input type='text' name='name'>
      <input type='submit' />
      </form>
    </body>
</html>
""".format(name))

