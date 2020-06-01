import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title('my window')
window.geometry('200x200')
def hit_me():
    messagebox.showinfo(title='Hi',message='hhhhh')
    messagebox.showwarning(title='Hi',message='nonono')
    messagebox.showerror(title='Hi',message='error')
    #   返回值为 yes 、 no
    messagebox.askquestion(title='Hi',message='?')
    #   返回值为 True、False
    messagebox.askyesno(title='Hi',message='?')
    #   返回值为 True、False
    messagebox.askretrycancel(title='Hi',message='?')
    #   返回值为 True、False
    messagebox.askokcancel(title='Hi',message='?')
tk.Button(window,text='hit me',command=hit_me).pack()

window.mainloop()