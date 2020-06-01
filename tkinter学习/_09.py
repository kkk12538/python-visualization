import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')

tk.Label(window,text='on the window',bg='red').pack()
frame=tk.Frame(window)
frame.pack()
l_frame=tk.Frame(frame)
r_frame=tk.Frame(frame)
l_frame.pack(side='left')
r_frame.pack(side='right')

tk.Label(l_frame,text='on the left frame1').pack()
tk.Label(l_frame,text='on the left frame2').pack()
tk.Label(r_frame,text='on the right frame').pack()

window.mainloop()