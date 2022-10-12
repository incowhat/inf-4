import tkinter

a = int(input('zadaj cislo strany: '))
apol = a>>1

canvas = tkinter.Canvas(width=a, height = a)
canvas.pack(fill="both")

for c in range(0, apol+4, 5):
    canvas.create_line(c, apol, apol, c+apol)
    canvas.create_line(c, apol, apol, -c+apol)
    canvas.create_line(-c+a, apol, apol, c+apol)
    canvas.create_line(-c+a, apol, apol, -c+apol)
    canvas.update()
    canvas.after(5)

tkinter.mainloop()