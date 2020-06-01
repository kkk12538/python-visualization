import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('500x500')

canvas=tk.Canvas(window,bg='blue',height=200,width=200,

                 )
canvas.pack()
image_file=tk.PhotoImage(file='1.gif')
#   anchor 为选中图片上的某角定于坐标上 nw、n、ne、center、w、e、se、sw
image=canvas.create_image(0,0,anchor='nw',image=image_file)
x0,y0,x1,y1=50,50,80,80
line=canvas.create_line(x0,y0,x1,y1)
oval=canvas.create_oval(x0,y0,x1,y1,fill='red')
arc=canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=180)
rect=canvas.create_rectangle(x0,y0,x1+50,y1+100,fill='black')
def moveit():
    #向上走两个单位
    canvas.move(rect,0,-2)
b=tk.Button(window,text='move',command=moveit)
b.pack()

window.mainloop()