import tkinter

canvas = tkinter.Canvas(width=320, height=400)
canvas.pack()

def oval(r, c, s):
    canvas.create_oval(160-r, 200-r, 160+r, 200+r, fill=c)
    canvas.create_text(175, 225-r, text=s, fill='orange')

def terc(event=None):
    global score
    score = 0

    canvas.delete('all')

    oval(150, 'black', 10)
    oval(100, 'white', 30)
    oval(50, 'black', 50)

    canvas.create_line(160, 40, 160, 360, fill='lightgrey')
    canvas.create_line(0, 200, 320, 200, fill='lightgrey')
    canvas.create_text(160, 375, text=f'Score: {score}', font='20', fill='red', tags='s')

def shot(event):
    global score
    x, y = event.x, event.y
    canvas.create_oval(x-5, y-5, x+5, y+5, fill='red')
    for r, s in [(150, 10), (100, 20), (50, 20)]:
        if r*r >= (x-160)**2 + (y-200)**2:
            score += s
            canvas.delete('s')
            canvas.create_text(160, 375, text=f'Score: {score}', font='20', fill='red', tags='s')

terc()

canvas.bind('<1>', shot)
canvas.bind_all('<Delete>', terc)
tkinter.mainloop()