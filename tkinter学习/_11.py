import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('300x200')

tk.Label(window,text=1).pack(side='top')
tk.Label(window,text=1).pack(side='bottom')
tk.Label(window,text=1).pack(side='left')
tk.Label(window,text=1).pack(side='right')


window.mainloop()