import tkinter
from random import randint

canvas = tkinter.Canvas(width=300, height = 300)
canvas.pack(fill="both")

r = 5
nevydalo = 0

for i in range(5000):
    x, y = randint(0, 300), randint(0, 300)
    if (x-150)**2 + (y-150)**2 <= 50**2:
        canvas.create_oval(x-r, y-r, x+r, y+r)
    canvas.update()


tkinter.mainloop()