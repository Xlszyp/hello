#!/usr/bin/python3
#-*-coding:UTF-8-*-

import tkinter as tk

#搭建框架

window=tk.Tk()
window.title('My window')
window.geometry('300x300')

#e=tk.Entry(window,show='*')
#e.pack()

#定义触发事件时的函数

def insert_point():
    var=e.get()
    t.insert('insert',var)

def insert_end():
    var=e.get()
    t.insert('end',var)
    #t.insert(2.2,var)

#创建按钮分别触发两种情况

b1=tk.Button(window,text='insert point',width=15,height=2,command=insert_point)
b1.pack()

b2=tk.Button(window,text='insert end',command=insert_end)
b2.pack()

#创建输入框entry,用户输入任何内容都显示*

e=tk.Entry(window,show='*')
e.pack()

#创建一个文本框用于显示

t=tk.Text(window,height=2)
t.pack()

window.mainloop()

