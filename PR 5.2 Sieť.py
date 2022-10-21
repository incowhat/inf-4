import tkinter, color

a = int(input('zadaj cislo strany: '))
apol = a>>1

canvas = tkinter.Canvas(width=a, height = a)
canvas.pack(fill="both")

def color(step=1, rgb=[255, 0, 0]):
    while True:
        for _ in range(step):
            for n in range(3):
                if rgb[n] == 255:
                    if rgb[n-1] != 0:
                        rgb[n-1] -= 1
                    elif rgb[n-2] < 255:
                        rgb[n-2] += 1
                    else:
                        rgb[n] -= 1
            
        yield f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

for c in range(0, apol+4, 5):
    canvas.create_line(c, apol, apol, c+apol, fill=next(color(6)))
    canvas.create_line(c, apol, apol, -c+apol, fill=next(color(6)))
    canvas.create_line(-c+a, apol, apol, c+apol, fill=next(color(6)))
    canvas.create_line(-c+a, apol, apol, -c+apol, fill=next(color(6)))
    canvas.update()
    canvas.after(50)

tkinter.mainloop()