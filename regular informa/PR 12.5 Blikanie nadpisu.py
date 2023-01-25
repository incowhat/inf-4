import tkinter, asyncio

canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

class Text:
    tasksPrechody = list()

    def __init__(self):
        canvas.create_text()
        Text.tasksPrechody.append(self.tag)
    
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
        await asyncio.gather(*Text.tasksPrechody)

size = 200
maxCanv = 3

Text()

asyncio.run(Text.call_tests())

tkinter.mainloop()