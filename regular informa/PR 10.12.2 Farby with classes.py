import tkinter, asyncio

class Prechod:
    p = list()
    gridX, gridY = 0, 0

    def __init__(self, color):
        self.color = color
        self.canvas = tkinter.Canvas(width=size, height=size)
        self.canvas.grid(row=Prechod.gridY, column=Prechod.gridX)
        Prechod.p.append(self.prechod())

        if Prechod.gridX == maxCanv-1:
            Prechod.gridX = 0
            Prechod.gridY += 1
        else:
            Prechod.gridX += 1
    
    @staticmethod
    def farba(value):
        return f'{int(value/size*255):02x}'

    async def prechod(self):
        for y in range(0, size+2, 2):
            for x in range(0, size+2, 2):
                self.canvas.create_rectangle(x, y, x+1, y+1, outline=self.color.format(x=self.farba(x), y=self.farba(y)))
                await asyncio.sleep(0)
            self.canvas.update()

    @staticmethod
    async def call_tests():
        await asyncio.gather(*Prechod.p)

size = 200
maxCanv = 3

Prechod('#{x}00{y}')
Prechod('#{y}{x}00')
Prechod('#00{y}{x}')
Prechod('#0000{x}')
Prechod('#00{y[0]}{y[0]}00')
Prechod('#{x[0]}{y[0]}{y[1]}{x[1]}{y[0]}{x[1]}')

asyncio.run(Prechod.call_tests())

tkinter.mainloop()