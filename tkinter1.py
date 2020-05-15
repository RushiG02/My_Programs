# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:40:52 2020

@author: Rushi
"""
import tkinter as tk
from datetime import datetime
window=tk.Tk()
window.title("welcome")
window.geometry('720x300')
text=tk.Label(window,text="hello")
text.grid(column=0,row=0)
def clicked():
    time=datetime.now().time()
    t="Button was clicked at "+str(time)
    text.configure(text=t)
     
btn=tk.Button(window,text="click here",command=clicked)
btn.grid(column=1,row=1)
window.mainloop()
