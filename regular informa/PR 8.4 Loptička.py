import tkinter as tk
import colorsys

tk.Tk().configure(bg='darkgrey')
cv = tk.Canvas(width=400, height=400, bg='grey')
cv.grid(column=0, row=0, columnspan=3)

ball = cv.create_oval(190, 190, 210, 210, fill='red', tags='ball')


def color_generator(step=1.0):
    while True:
        for i in range(int(1528/step)):
            hue = i / int(1528/step)
            r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
            yield f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'
color = color_generator(5)


def move(x, y):
    while True:
        cv.move('ball', x, y)
        cv.itemconfigure('ball', fill=next(color))
        cv.after(2)
        cv.update()

        bc = cv.coords('ball')
        if bc[0] <= 0 or bc[1] <= 0 or bc[2] >= 400 or bc[3] >= 400:
            x, y = -x, -y


bHore = tk.Button(text='Hore', width=8, command=lambda: move(0, -1))
bHore.grid(column=1, row=1)
bVlavo = tk.Button(text='Vlavo', width=8, command=lambda: move(-1, 0))
bVlavo.grid(column=0, row=2)
bVpravo = tk.Button(text='Vpravo', width=8, command=lambda: move(1, 0))
bVpravo.grid(column=2, row=2)
bDole = tk.Button(text='Dole', width=8, command=lambda: move(0, 1))
bDole.grid(column=1, row=3)

tk.mainloop()
