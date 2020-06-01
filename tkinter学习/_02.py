import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('400x400')

e1=tk.Entry(window,show=None)
#   e1=tk.Entry(window,show='*')
e1.pack()

def insert_point():
    var=e1.get()
    t1.insert('insert',var)

def insert_precision():
    var=e1.get()
    #插入到第一行的第一列后
    t1.insert(1.1,var)

def insert_end():
    var=e1.get()
    t1.insert('end',var)


#全部删除
def clear_all():
    t1.delete(1.0,4.0)

b1=tk.Button(window,text='insert point',command=insert_point)
b2=tk.Button(window,text='insert precision',command=insert_precision)
b3=tk.Button(window,text='insert end',command=insert_end)
b4=tk.Button(window,text='clear all',command=clear_all)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
t1=tk.Text(window,height=3)
t1.pack()
window.mainloop()