import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('300x200')

# 四行三列
#ipadx  ipady
#padx pady 扩展
for i in range(4):
    for j in range(3):
        tk.Label(window,text=1).grid(row=i,column=j,
                                     padx=10,pady=10,
                                     #ipadx=10,ipady=10,
                                     )







window.mainloop()