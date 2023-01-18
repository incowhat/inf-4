import tkinter, asyncio

class Prechod:
    tasksPrechody = list()
    gridX, gridY = 0, 0

    def __init__(self, color):
        self.color = color
        self.canvas = tkinter.Canvas(width=size, height=size)
        self.canvas.grid(row=Prechod.gridY, column=Prechod.gridX)
        Prechod.tasksPrechody.append(self.prechod())

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
            
            self.canvas.update()
            await asyncio.sleep(0)

    @staticmethod
    async def call_tests():
        await asyncio.gather(*Prechod.tasksPrechody)

size = 200
maxCanv = 3

Prechod('#{x}00{y}')
Prechod('#{y}{x}00')
Prechod('#00{y}{x}')
Prechod('#{x[0]}000{y[0]}{y[0]}')
Prechod('#0000{x}')
Prechod('#00{y[0]}{y[0]}00')
Prechod('#{x[0]}{y[1]}ff{y}')
Prechod('#{y[0]}{x[1]}{y[0]}{x[1]}{y[0]}{x[1]}')
Prechod('#{x[0]}{y[0]}{y[1]}{x[1]}{y[0]}{x[1]}')

asyncio.run(Prechod.call_tests())

tkinter.mainloop()