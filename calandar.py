
import tkinter as tk
from tkinter import ttk
import calendar

window=tk.Tk()
window.title("calender")
window.geometry('200x200')
style=ttk.Style()
style.map('c.TButton',
          foreground=[('pressed','red'),('active','blue')]
          )

yearlist=[i for i in range(1900,3000)]
window.month=1
window.year=int(yearlist[0])
variable = tk.StringVar(window)
variable.set(yearlist[0])

w = ttk.Combobox(window, textvariable=variable, values=yearlist)
w.grid(column=1,row=0)
#opt = tk.OptionMenu(window, variable, *yearlist ).grid(column=1,row=0)

def xx(*args):
    window.year=int(variable.get())
    text.configure(text=str((calendar.month(window.year,window.month))))
variable.trace("w",xx)




text=tk.Label(window,text=str((calendar.month(window.year,window.month))))
text.grid(column=1,row=1)
def nxt():
    window.month+=1
    if window.month==13:
        window.month=1
        window.year+=1
    text.configure(text=str((calendar.month(window.year,window.month))))
def prev():
    window.month-=1
    if window.month==0:
        window.month=1
        window.year-=1
    text.configure(text=str((calendar.month(window.year,window.month))))

b1=ttk.Button(window,text='<',style='c.TButton',width=3,command=prev).grid(column=0,row=1)
b2=ttk.Button(window,text='>',style='c.TButton',width=3,command=nxt).grid(column=3,row=1)
window.mainloop()