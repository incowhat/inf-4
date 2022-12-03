import tkinter, asyncio
from random import shuffle, randint

pocet = 300
cisla = list(range(1, pocet+1))
shuffle(cisla)
cisla2=list(cisla)

selection = tkinter.Canvas(width=pocet, height=pocet, bg='black')
selection.grid(column=0, row=0)
selection.update()

half = tkinter.Canvas(width=pocet, height=pocet, bg='black')
half.grid(column=1, row=0)
half.update()


def vykreslenie(canvas, pole):
    canvas.delete('all')
    for i, c in enumerate(pole):
        canvas.create_line(i, pocet, i, pocet-c, fill='white')
    canvas.update()

def posun(canvas, x, y, fill='red'):
    canvas.create_line(x, pocet, x, pocet-y, fill=fill)
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
    



async def selectionSort(pole):
    for i in range(pocet):
        zmenCislo = minimum(pole[i:])
        cisloIndx = pole.index(zmenCislo)
        posun(selection, cisloIndx, zmenCislo)
        posun(selection, zmenCislo, zmenCislo, fill='green')
        pole.insert(i, pole.pop(cisloIndx))

        vykreslenie(selection, pole)
        await asyncio.sleep(0) 

async def mojTestSort(docasny, hlavny=[]):
    if not hlavny:
        hlavny = list(docasny)
    if len(docasny) == 1:
        return

    docasny2 = tuple(docasny)
    rozpatie = priemer(docasny2)

    for i in docasny2:
        cisloIndxDocasny = docasny.index(i)
        cisloIndxHlavny = hlavny.index(i)

        if i <= rozpatie:
            posun(half, cisloIndxHlavny, i)
            posun(half, i, i, fill='green')
            
            docasny.insert(0, docasny.pop(cisloIndxDocasny))
            hlavny.insert(minimum(docasny)-1, hlavny.pop(cisloIndxHlavny))
        else:
            posun(half, cisloIndxHlavny, i)
            posun(half, i, i, fill='green')
            
            if (mD := maximum(docasny)) < pocet:
                docasny.insert(mD-1, docasny.pop(cisloIndxDocasny))
                hlavny.insert(mD-1, hlavny.pop(cisloIndxHlavny))
            else:
                docasny.append(docasny.pop(cisloIndxDocasny))
                hlavny.append(hlavny.pop(cisloIndxHlavny))

        vykreslenie(half, hlavny)
        await asyncio.sleep(0)

    if (dlzka := len(docasny)) > 2:
        dlzka = int((dlzka+1)/2)
        await mojTestSort(docasny[:dlzka], hlavny)
        await mojTestSort(docasny[dlzka:], hlavny)



async def call_tests():
    await asyncio.gather(selectionSort(cisla), mojTestSort(cisla2))
asyncio.run(call_tests())

tkinter.mainloop()