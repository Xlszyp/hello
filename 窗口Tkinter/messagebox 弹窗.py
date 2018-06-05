#!/usr/bin/python3
#-*-coding:UTF-8-*-

import tkinter as tk
import tkinter.messagebox

window=tk.Tk()
window.title('My window')
window.geometry('200x200')

def hit_me():
    tk.messagebox.showinfo(title='Hi',message='Hahahahahaha~')  #return 'ok'
    tk.messagebox.showwarning(title='Hi',message='Nononono~')   #return 'ok'
    tk.messagebox.showerror(title='Hi',message='NO!never.')     #return 'ok'
    print(tk.messagebox.askquestion(title='Hi',message='23333~'))      #return 'yes','no'
    print(tk.messagebox.askyesno(title='Hi', message='hahahaha_1'))   # return True, False

    print(tk.messagebox.askokcancel(title='Hi', message='hahahaha_2'))   # return True, False
    print(tk.messagebox.askyesnocancel(title="Hi", message="haha3"))     # return, True, False, None


tk.Button(window,text='Hit me',command=hit_me).pack()
window.mainloop()
