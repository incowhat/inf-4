import tkinter

a = int(input('zadaj cislo strany: '))
rgb = [0, 0, 255]
color = lambda: f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

canvas = tkinter.Canvas(width=a, height = a)
canvas.pack(fill="both")

for i in range(1, (a>>1)+2):
    canvas.create_rectangle(i, i, a, a, outline=color())
    a -= 1
    for j in range(3):
        for n in range(3):
            if rgb[n] == 255:
                if rgb[n-1] != 0:
                    rgb[n-1] -= 1
                elif rgb[n-2] < 255:
                    rgb[n-2] += 1
                else:
                    rgb[n] -= 1
                
    canvas.update()
    canvas.after(10)

tkinter.mainloop()