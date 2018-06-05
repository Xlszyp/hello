#!/usr/bin/python3
#-*-coding:UTF-8-*-


import tkinter as tk

window=tk.Tk()
window.title('Welcome to 2333 Python')
window.geometry('450x300')

#幕布的创建,welcome image
canvas=tk.Canvas(window,height=200,width=500)
image_file=tk.PhotoImage(file='welcome.gif')
image=canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

#创建两个label
tk.Label(window,text='User name:').place(x=50,y=150)
tk.Label(window,text='Password:').place(x=50,y=190)

#创建输入框
var_usr_name=tk.StringVar() #定义var_usr_name
var_usr_name.set('23333@python.com')
var_usr_pwd=tk.StringVar()

entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=150)

entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160,y=190)

def usr_login():
    pass

def usr_sign_up():
    pass
#创建Button
btn_login=tk.Button(window,text='Login',command=usr_login)
btn_login.place(x=170,y=230)

btn_sign_up=tk.Button(window,text='Sign up',command=usr_sign_up)
btn_sign_up.place(x=270,y=230)

window.mainloop()
