import tkinter
from random import randint, choice

canvas = tkinter.Canvas(width=500, height=400, bg='#9acd32')
canvas.pack()

def strom(event):
    x, y = event.x, event.y

    canvas.create_line(x, y, x, y+randint(50, 80), width=randint(10, 30), fill=choice(('#cd853f', '#8b4513', '#a52a2a')))
    canvas.create_oval(x-int(w:=randint(50,80))//2, y-randint(50, 100)+10, x+(w-w//2), y+10, fill=choice(('#008000', '#006400', '#90ee90')), outline='#003000')


canvas.bind('<1>', strom)
canvas.bind_all('<Delete>', lambda event: canvas.delete('all'))
tkinter.mainloop()