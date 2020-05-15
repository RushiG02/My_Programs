import tkinter



window = tkinter.Tk()
window.title("GUI")
window.geometry('300x300')
window.c=0
def clo():
    window.destroy()
        

def color():
    if window.c>5:
        window.c=0
    
    if window.c==0:
        window.configure(bg='yellow')
        
    elif window.c==1:
        window.configure(bg='red')
        
    elif window.c==3:
        window.configure(bg='green')
        
    elif window.c==4:
        window.configure(bg='blue')
        
    else:
        window.configure(bg='orange')
    
    window.c+=1
    
b=tkinter.Button(window,text='change color',command=color).pack()
tkinter.Button(window,text='close',command=clo).pack()
window.mainloop()