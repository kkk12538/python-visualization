import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('300x200')

var=tk.StringVar()
l1=tk.Label(window,bg='yellow',width=20,text='empty')
l1.pack()

def print_selectiong():
    #修改l1的所有参数
    l1.config(text='you have selected'+var.get())

#variable是选中的值
r1 =tk.Radiobutton(window,text='Option A',variable=var,
                   value='A',command=print_selectiong)
r1.pack()
r2 =tk.Radiobutton(window,text='Option B',variable=var,
                   value='B',command=print_selectiong)
r2.pack()
r3 =tk.Radiobutton(window,text='Option C',variable=var,
                   value='C',command=print_selectiong)
r3.pack()
window.mainloop()