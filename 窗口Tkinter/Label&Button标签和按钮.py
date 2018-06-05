#!/usr/bin/python3
#-*-coding:UTF-8-*-

print('++++++Lable&Button++++++')

import tkinter as tk

#窗口主体框架
window=tk.Tk()
window.title('My window')
window.geometry('300x200')

#窗口的内容
#window.mainloop()

'''
l=tk.Label(window,
           text='OMG!this is xls!',     #标签的文字
           bg='blue',   #背景颜色
           font=('Arial',12),   #字体和字体大小
           width=15,height=2    #标签长宽
           )

l.pack()    #固定窗口位置

'''
var=tk.StringVar()  #这是文字变量存储器
l=tk.Label(window,
           textvariable=var,     #使用textvariable替换text,因为可变化
           bg='blue',font=('Arial',12),width=15,height=2)
l.pack()



on_hit=False    #默认初始状态为false

def hit_me():
    global on_hit

    if on_hit==False:
        on_hit=True
        var.set('you hit me!')
    else:
        on_hit=False
        var.set('surprised...')
        

b=tk.Button(window,
            text='hit me',   #显示按钮上的文字
            width=10,height=2,
            command=hit_me) #点击按钮式执行的命令
b.pack()    #按钮位置

window.mainloop()   #运行这个窗口
