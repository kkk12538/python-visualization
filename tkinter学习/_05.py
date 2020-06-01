import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('300x200')


l1=tk.Label(window,bg='yellow',width=20,text='empty')
l1.pack()
def print_selection(v):
    l1.config(text='you have selected'+v)
#   resoulution=0.01保留两位小数
#   showvalue显示scale上的值
#   _from,to 范围
#   tickinterval 显示刻度
s=tk.Scale(window,label='try me',from_=5,to=11,
           orient=tk.HORIZONTAL,length=200,showvalue=0,
           tickinterval=3,resolution=0.01,command=print_selection)
s.pack()



window.mainloop()