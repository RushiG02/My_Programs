import random
import tkinter as tk
from tkinter import messagebox  
window=tk.Tk()
window.title("guessing game")
window.geometry('500x300')
window.resizable(0,0)
window.configure(bg='LightCyan2')

window.n=random.randint(100,999)

l,m,f=0,0,0
lbl1=tk.Label(window,text='you have to guess 3-digit number in 5 chances',bg="LightCyan2")
lbl1.grid(column=0,row=0)
l1=tk.Label(window,text='guess = ',bg="LightCyan2")
l1.grid(column=0,row=3)
a1=tk.Entry(window)
a1.grid(column=1,row=3)

window.c=0
window.l,window.m,window.f=0,0,0
def check():
    
    window.c+=1
    
    if 5-window.c==0:
        
        messagebox.showerror("error",'0 chances left')
        messagebox.showinfo("Number",'The number is: '+str(window.n))
        messagebox.showinfo("score",(window.l+window.m+window.f)*33.334)
        
        window.destroy()
        return
    lbl1=tk.Label(window,text=str(5-window.c)+'chances left',bg="LightCyan2")
    lbl1.grid(column=0,row=1)
    
    g=int(a1.get())
    
    if g==window.n:
        messagebox.showinfo("congo!!","you won!!!") 
        messagebox.showinfo("score",100)
        window.destroy()
    else:
        if g<window.n:
            messagebox.showwarning("warning","guess is less than no")
            
        else:
            messagebox.showwarning("warning","guess is grater than no")
        t=window.n
        for j in range(3):
            if t%10==g%10:
                if j==0:
                    messagebox.showinfo("congo!!","last no is right")
                    window.l=1
                elif j==1:
                    messagebox.showinfo("congo!!","middle no is right")
                    window.m=1
                else:
                    messagebox.showinfo("congo!!","first no is right")
                    window.f=1            
            t=t//10
            g=g//10
    
     

tk.Button(window,text='check',command=check).grid(column=1,row=4)
window.mainloop()


    