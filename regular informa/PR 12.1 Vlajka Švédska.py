import tkinter
from random import randint

r = 5

canvas = tkinter.Canvas(width=400, height=250)
canvas.pack(fill='both', expand=True)
canvas.update()
width, height = canvas.winfo_width(), canvas.winfo_height()

while True:
    if width != canvas.winfo_width() or height != canvas.winfo_height():
        width, height = canvas.winfo_width(), canvas.winfo_height()
        canvas.delete('all')
    
    x, y = randint(r, width-r), randint(r, height-r)

    if width/5*1.25 < x < width/5*2 or height/5*2 < y < height/5*3:
            color = 'gold'
    else:
        color = 'navy'

    canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline='')
    canvas.update()
    canvas.after(1)