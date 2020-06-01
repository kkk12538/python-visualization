import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('500x500')

l=tk.Label(window,text='',bg='red')
l.pack()
count=0
def do_job():
    global count
    l.config(text='do {}'.format(count))
    count+=1


menubar=tk.Menu(window)
# tearoff 能否被分开
file_menu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='file',menu=file_menu)
file_menu.add_cascade(label='New',command=do_job)
file_menu.add_cascade(label='Open',command=do_job)
file_menu.add_cascade(label='Save',command=do_job)
# 添加分割线
file_menu.add_separator()

file_menu.add_command(label='Exit',command=window.quit)

edit_menu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_cascade(label='Cut',command=do_job)
edit_menu.add_cascade(label='Copy',command=do_job)
edit_menu.add_cascade(label='Paste',command=do_job)

sub_menu=tk.Menu(file_menu,tearoff=0)
file_menu.add_cascade(label='Import',menu=sub_menu,underline=0)
sub_menu.add_command(label='Submenu1',command=do_job)

window.config(menu=menubar)


window.mainloop()