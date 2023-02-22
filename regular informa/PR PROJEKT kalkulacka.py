import tkinter

class Button:
    def __init__(self, text: str, column: int, row: int, width: int, height: int, func=None):
        self.func = func
        self.text = text
        self.button = tkinter.Button(text=text, width=width, height=height, command=self.command)
        self.button.grid(column=column, row=row)
        self.button.bind_all(f'<KeyPress-{text}>', self.invoke)
        
    def invoke(self, event):
        self.button.invoke()

    def command(self):
        if self.func:
            pass
        else:
            entry.configure(state='normal')
            entry.insert('end', self.text)
            entry.configure(state='readonly')

tkinter.Tk().title('Kalkulacka')
entry = tkinter.Entry(font='10', justify='right', state='readonly')
entry.grid(column=0, row=1, columnspan=3)

b9 = Button('9', 2, 2, 10, 2)
b8 = Button('8', 1, 2, 10, 2)
b7 = Button('7', 0, 2, 10, 2)
b6 = Button('6', 2, 3, 10, 2)
b5 = Button('5', 1, 3, 10, 2)
b4 = Button('4', 0, 3, 10, 2)
b3 = Button('3', 2, 4, 10, 2)
b2 = Button('2', 1, 4, 10, 2)
b1 = Button('1', 0, 4, 10, 2)
b0 = Button('0', 0, 5, 10, 2)
bComma = Button(',', 1, 5, 10, 2)


tkinter.mainloop()