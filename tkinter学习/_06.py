import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('300x200')

l1=tk.Label(window,bg='yellow',width=20,text='')
l1.pack()

def print_selection():
    if var1.get()==0 and var2.get()==0:
        l1.config(text='I like neither!')
    elif var1.get()==1 and var2.get()==1:
        l1.config(text='I like both!')
    elif var1.get()==0 and var2.get==1:
        l1.config(text='I like C++!')
    else:
        l1.config(text='I like Python!')


var1=tk.IntVar()
var2=tk.IntVar()
c1=tk.Checkbutton(window,text='Python',variable=var1,
                  onvalue=1,offvalue=0,command=print_selection)
c2=tk.Checkbutton(window,text='C++',variable=var2,
                  onvalue=1,offvalue=0,command=print_selection)
c1.pack()
c2.pack()

window.mainloop()