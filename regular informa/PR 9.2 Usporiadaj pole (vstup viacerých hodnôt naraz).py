import tkinter
from random import shuffle

pocet = 300
size = 4
ratio = 2
cisla = list(range(1, pocet+1))
shuffle(cisla)

canvas = tkinter.Canvas(width=pocet*size, height=pocet*size/ratio, bg='black')
canvas.pack()
canvas.update()
width = canvas.winfo_height()

def color(step=1, rgb=[255, 0, 0]):
    def generator():
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
    
    return [next(generator()) for _ in range(pocet)]

farby = color(1200//pocet)

def vykreslenie(pole):
    canvas.delete('all')
    for i, y in enumerate(pole):
        canvas.create_line(i*size+size, width, i*size+size, width-y*size/ratio, width=size, fill=farby[y-1])

    canvas.update()

def posun(x, y, fill='white'):
    canvas.create_line(x*size+size, width, x*size+size, width-y*size/ratio, width=size, fill=fill)
    canvas.update()

def minimum(pole):
    mini = pole[0]
    for i in pole[1:]:
        if i < mini:
            mini = i
    return mini

def maximum(pole):
    maxi = pole[0]
    for i in pole[1:]:
        if i > maxi:
            maxi = i
    return maxi

def priemer(pole):
    sucet = 0
    dlzka = 0
    for i in pole:
        sucet += i
        dlzka += 1

    return sucet/dlzka

def selectionSort(pole):
    for i in range(pocet-1):
        zmenCislo = minimum(pole[i:])
        cisloIndx = pole.index(zmenCislo)
        posun(cisloIndx, zmenCislo)
        posun(zmenCislo, zmenCislo)
        pole.insert(i, pole.pop(cisloIndx))

        vykreslenie(pole)



selectionSort(cisla)

tkinter.mainloop()