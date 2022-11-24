import tkinter
from random import randint

canvas = tkinter.Canvas(width=400, height = 400)
canvas.pack(fill='both', expand=True)
width, height = canvas.winfo_width(), canvas.winfo_height()
points = list()

def priamka(event):
    if len(points)>4:
        return

    points.append((event.x, event.y))
    canvas.delete('ciary')

    if len(points)//2:
        for i in range(0, 1+len(points)//2, 2):
            canvas.create_line(points[i], points[i+1], tags='ciary')
            canvas.create_oval(points[i][0]+5, points[i][1]+5, points[i][0]-5, points[i][1]-5, tags='ciary')
            canvas.create_oval(points[i+1][0]+5, points[i+1][1]+5, points[i+1][0]-5, points[i+1][1]-5, tags='ciary')

canvas.bind('<1>', priamka)

while True:
    try:
        if width != canvas.winfo_width() or height != canvas.winfo_height():
            width, height = canvas.winfo_width(), canvas.winfo_height()
            canvas.delete('legenda')
            points.clear()

            size = ((width*height)>>15)+5
            canvas.create_text(width/2, height-height//4, text='priesecnik - stlac <p>', font=f'Consolas {size}', tags='legenda')
            canvas.create_text(width/2, height+size*2-height//4, text='vycistenie plochy - stlac <Delete>', font=f'Consolas {size}', tags='legenda')

            canvas.update()

        canvas.update()
    
    except: exit() if tkinter.TclError else None