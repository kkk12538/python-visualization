import tkinter as tk


window =tk.Tk()
window.title('my window')
window.geometry('500x200')

#创建tk的字符串变量
var=tk.StringVar()

l1=tk.Label(window,textvariable=var,bg='green',font=('Arial',12),
            width=15,height=2)
#放置
l1.pack()

on_hit=False
def hit_me():
    global on_hit
    if on_hit==False:
        var.set('you hit me')
        on_hit=True
    else:
        var.set('')
        on_hit=False
b1=tk.Button(window,text='hit me',width='15',height='2',command=hit_me)
b1.pack()
#刷新
window.mainloop()