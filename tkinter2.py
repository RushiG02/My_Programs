# -*- coding: utf-8 -*-
"""
Created on Fri May  1 10:48:30 2020

@author: Rushi
"""

import tkinter as tk
window=tk.Tk()
window.geometry('300x300')
window.resizable(0,0)

l1=tk.Label(window,text='a1= ')
l1.grid(column=0,row=0)
a1=tk.Entry(window)
a1.grid(column=1,row=0)
l2=tk.Label(window,text='a2= ')
l2.grid(column=0,row=1)
a2=tk.Entry(window)
a2.grid(column=1,row=1)
l3=tk.Label(window,text="Result")
l3.grid(row=2,column=0)
t3=tk.Entry(window)
t3.grid(row=2,column=1)
a1.insert(0,0)
a2.insert(0,0)
def clr():
    a1.delete(0,"end")
    a2.delete(0,"end")
    t3.delete(0,"end")
tk.Button(window,text='C',command=clr).grid(column=2,row=2)
def add():
    t3.delete(0,"end")
    a=int(a1.get())
    b=int(a2.get())
    c=a+b
    t3.insert(1,c)
    
def minu():
    t3.delete(0,"end")
    a=int(a1.get())
    b=int(a2.get())
    c=a-b
    t3.insert(1,c)
    
def mult():
    t3.delete(0,"end")
    a=int(a1.get())
    b=int(a2.get())
    c=a*b
    t3.insert(1,c)
    
def div():
    t3.delete(0,"end")
    a=int(a1.get())
    b=int(a2.get())
    c=a/b
    t3.insert(1,c)
    
def pow1():
    t3.delete(0,"end")
    a=int(a1.get())
    b=int(a2.get())
    c=a**b
    t3.insert(1,c)
    
l=tk.Label(window,text='').grid(column=0,row=3)    
tk.Button(window,text='+',command=add).grid(column=0,row=4)
tk.Button(window,text='-',command=minu).grid(column=1,row=4)
tk.Button(window,text='*',command=mult).grid(column=2,row=4)
l=tk.Label(window,text='').grid(column=0,row=5)  
tk.Button(window,text='/',command=div).grid(column=0,row=6)
tk.Button(window,text='^',command=pow1).grid(column=1,row=6)
window.mainloop()