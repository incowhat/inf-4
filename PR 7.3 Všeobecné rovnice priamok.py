import tkinter
from random import randint

canvas = tkinter.Canvas(width=400, height = 400)
canvas.pack(fill="both", expand=True)
width, height = canvas.winfo_width(), canvas.winfo_height()
points = list()


def priamka(event):
    global point
    if len(points)>4:
        return

    points.append([event.x, event.y])




canvas.bind('<1>', priamka)

while True:
    if width != canvas.winfo_width() or height != canvas.winfo_height():
        width, height = canvas.winfo_width(), canvas.winfo_height()
        canvas.delete('legenda')

        size = ((width*height)>>15)+5
        canvas.create_text(width/2, height-height//4, text='priesecnik - stlac <p>', font=f'Consolas {size}', tags='legenda')
        canvas.create_text(width/2, height+size*2-height//4, text='vycistenie plochy - stlac <Delete>', font=f'Consolas {size}', tags='legenda')



        canvas.update()

    canvas.update()