#!/usr/bin/python3
#-*-coding:UTF-8-*-

import tkinter as tk

window=tk.Tk()
window.title('My window')
window.geometry('200x200')


l=tk.Label(window,text='233',bg='yellow')
l.pack()

counter=0
def do_job():
    global counter
    l.config(text='do '+str(counter))
    counter+=1
    
#创建一个菜单条，放File,Edit菜单
menubar=tk.Menu(window)

#创建一个放File菜单的菜单条filemenu，属于menubar
filemenu=tk.Menu(menubar,tearoff=0)

#在menubar菜单条中添加File菜单，属于filemenu
menubar.add_cascade(label='File',menu=filemenu)

#在filemenu菜单条的File菜单中添加次菜单
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)


editmenu=tk.Menu(menubar,tearoff=0)

menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

submenu=tk.Menu(filemenu)
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
submenu.add_command(label='Submenu1',command=do_job)

xls=tk.Menu(submenu)
submenu.add_cascade(label='num',menu=xls,underline=0)
xls.add_command(label='xls',command=do_job)

#激活菜单
window.config(menu=menubar)

window.mainloop()

