#!/usr/bin/python3
#-*-coding:UTF-8-*-

import tkinter as tk

window=tk.Tk()
window.title('My window')
window.geometry('500x500')


l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()


def print_selection(v):
    l.config(text='you have selected '+v)


s = tk.Scale(window, label='try me', from_=0, to=20, orient=tk.HORIZONTAL,length=400, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)


s.pack()

window.mainloop()
