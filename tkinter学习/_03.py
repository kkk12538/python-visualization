import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x300')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=8, textvariable=var1)
l.pack()

#在label上输出指针选中的值
def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)


b1 = tk.Button(window, text='print selection', command=print_selection)
b1.pack()
var2 = tk.StringVar()
# 列表、元组...
var2.set((11, 22, 33, 44))
lb = tk.Listbox(window, listvariable=var2)
list1 = [1, 2, 3, 4]
for i in list1:
    lb.insert('end', i)

lb.insert(0, 'first')
lb.insert(1, 'second')
lb.pack()
window.mainloop()
