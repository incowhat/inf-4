import tkinter as tk

tk.Tk().configure(bg='darkgrey')
cv = tk.Canvas(width=400, height=400, bg='grey')
cv.grid(column=0, row=0, columnspan=3)

cv.create_oval(190, 190, 210, 210, fill='red', tags='ball')


def move(x, y):
    cv.move('ball', x, y)
    cv.update()



bHore = tk.Button(text='Hore', width=8, command=move)
bHore.grid(column=1, row=1)
bVlavo = tk.Button(text='Vlavo', width=8, command=move)
bVlavo.grid(column=0, row=2)
bVpravo = tk.Button(text='Vpravo', width=8, command=move)
bVpravo.grid(column=2, row=2)
bDole = tk.Button(text='Dole', width=8, command=move)
bDole.grid(column=1, row=3)

tk.mainloop()
