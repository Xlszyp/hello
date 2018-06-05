#!/usr/bin/python3
#-*-coding:UTF-8-*-

import tkinter as tk

window=tk.Tk()
window.title('My window')
window.geometry('200x200')

#在window上创建一个标签
tk.Label(window,text='on the window').pack()

#在window上创建一个窗口frm
frm=tk.Frame(window)
frm.pack()

#在frm窗口上创建frm_l,frm_r小窗口
frm_l=tk.Frame(frm,)
frm_r=tk.Frame(frm,)

#pack显示小窗口所在的左和右的位置
frm_l.pack(side='left')
frm_r.pack(side='right')

#在frm_l,frm_r小窗口上创建标签
tk.Label(frm_l,text='on the frm_l1').pack()
tk.Label(frm_l,text='on the frm_l2').pack()

tk.Label(frm_r,text='on the frm_r1').pack()
tk.Label(frm_r,text='on the frm_r2').pack()

window.mainloop()
