import tkinter

canvas = tkinter.Canvas(width=300, height = 300)
canvas.pack(fill="both")

for c in range(0, 151, 5):
    canvas.create_line(c, 150, 150, c+150)
    canvas.create_line(c, 150, 150, -c+150)
    canvas.create_line(-c+300, 150, 150, c+150)
    canvas.create_line(-c+300, 150, 150, -c+150)
    canvas.update()
    # canvas.after(200)

tkinter.mainloop()