import tkinter
from random import randint

total = int(input('pocet pismen: '))

canvas = tkinter.Canvas(width=400, height = 400)
canvas.pack(fill="both", expand=True)
width, height = canvas.winfo_width(), canvas.winfo_height()

while True:
    if width != canvas.winfo_width() or height != canvas.winfo_height():
        width, height = canvas.winfo_width(), canvas.winfo_height()
        canvas.delete("all")

        for _ in range(total):
            x, y = randint(0, width), randint(0, height)
            
            if x < width/2:
                text, color = ('A', '#ff2200') if (y < height/2) else ('B', '#0022ff')
            else:
                text, color = ('C', '#00ff22') if (y < height/2) else ('D', '#ffcc00')

            canvas.create_text(x, y, text=text, fill=color, font=f'Comic {((width*height)>>14)+10}')
            canvas.update()

    canvas.update()