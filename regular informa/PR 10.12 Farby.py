import tkinter, asyncio

size = 200
c1, c2, c3 = [tkinter.Canvas(width=size, height=size) for _ in range(3)]
c1.grid(row=0, column=0); c2.grid(row=0, column=1); c3.grid(row=0, column=2)
# 3 canvasy

def farba(hodnota):
    return f'{int(hodnota/size*255):02x}'
    # podla pozicie na osi vytvori farbu 0-255 v hex 0-ff

async def prechod(canvas, color):
    for y in range(0, size+2, 2):
        for x in range(0, size+2, 2):
            canvas.create_rectangle(x, y, x+1, y+1, outline=color.format(x=farba(x), y=farba(y)))
            await asyncio.sleep(0)
        canvas.update()
    # funkcia ktora na danu plochu vykresli prechod farieb podla zadaneho kluca
    # dve farby s osou vo forme hex farebneho kodu, tretia farba je 00 byte

async def call_tests():
    await asyncio.gather(prechod(c1, '#{x}00{y}'), prechod(c2, '#{y}{x}00'), prechod(c3, '#00{y}{x}'))
asyncio.run(call_tests())
# async spusti funkciu 3 krat s roznimi farebnymi prechodmi
# async => 3 kopie funkcie sa striedaju medzi sebou (vo funkcii vidime kde sa striedaju - await)

tkinter.mainloop()