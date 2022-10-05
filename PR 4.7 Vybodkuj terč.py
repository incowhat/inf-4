import tkinter
from random import randint

canvas = tkinter.Canvas(width=300, height = 300)
canvas.pack(fill="both")

r = 5
nevydalo = 0

for i in range(10000):
    x, y = randint(0, 300), randint(0, 300)
    kruh = lambda: (x-150)**2 + (y-150)**2 

    if 50**2 < kruh() <= 100**2:
        color = 'white'
    elif 150**2 < kruh():
        nevydalo += 1
        continue
    else:
        color = 'black'

    canvas.create_oval(x-r, y-r, x+r, y+r, fill=color)
    # canvas.update()

canvas.create_text(275, 280, text=nevydalo, fill='#ee2200', font='30')
print(nevydalo)
print(nevydalo/10000)
tkinter.mainloop()