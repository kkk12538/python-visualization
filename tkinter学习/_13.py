import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('300x200')

tk.Label(window,text=1).place(x=10,y=100,anchor='nw')






window.mainloop()