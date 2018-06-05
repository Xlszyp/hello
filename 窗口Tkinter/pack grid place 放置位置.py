#!/usr/bin/python3
#-*-coding:UTF-8-*-

import tkinter as tk

window=tk.Tk()
window.title('Mywidow')
window.geometry('200x200')

#tk.Label(window,text='1').pack(side='top')  #上
#tk.Label(window,text='2').pack(side='bottom')   #下
#tk.Label(window,text='3').pack(side='left') #左
#tk.Label(window,text='4').pack(side='right')    #右



for i in range(4):
    for j in range(3):
        tk.Label(window,text='x').grid(row=i,column=j,padx=10,pady=10)


tk.Label(window,text=1).place(x=20,y=10,anchor='nw')


window.mainloop()
