import tkinter

canvas = tkinter.Canvas(width=300, height=100, bg='white')
canvas.grid(column=0, row=0, rowspan=3)

def click():
    farba = e1.get()
    velkost = int(e2.get())

    canvas.delete('all')
    s=f'Ariel {velkost} bold'
    canvas.create_text(150,50, text='AHOJ', fill=farba, font=s)

l1 = tkinter.Label (text='Farba', width=7, anchor='nw')
l1.grid(column=1, row=0)
l2 = tkinter.Label (text='Velkosť', width=7, anchor='nw')
l2.grid(column=1, row=1)

e1 = tkinter.Entry(width=15)
e1.grid(column=2, row=0)

e2 = tkinter.Entry(width=15)
e2.grid(column=2, row=1)

b = tkinter.Button(text='Piš AHOJ', width=22, command=click)

b.grid(column=1, row=2, columnspan=2)

tkinter.mainloop()