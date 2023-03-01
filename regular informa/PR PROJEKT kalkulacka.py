import tkinter

class Button:
    instances = []

    def __init__(self, text: str, column: int, row: int, func=None, key=None):
        self.func = func
        self.text = text
        self.key = key if key else text

        self.button = tkinter.Button(text=text, command=self.command, justify='center')
        self.button.configure(fg='#303030', bg='#f0f0f0', relief='groove', activebackground='darkgrey')
        self.button.grid(column=column, row=row, sticky="WENS")
        
        self.button.bind_all(f'<KeyPress-{self.key}>', self.invoke)
        self.button.bind('<Enter>', self.hover)
        self.button.bind('<Leave>', self.hover)

        Button.instances.append(self)
        
    def invoke(self, event):
        self.button.invoke()

    def hover(self, event):
        if str(event)[1:6] == 'Enter':
            self.button.configure(fg='black', bg='lightgrey')
        else:
            self.button.configure(fg='#303030', bg='#f0f0f0')

    def size(self):
        window.grid_columnconfigure('all', weight=1)
        window.grid_rowconfigure('all', weight=1)
        txtSize = 12 + (window.winfo_width()+window.winfo_height())//90
        self.button.configure(font=('Calibri', txtSize))
        entry.configure(font=('Calibri', txtSize))

    @staticmethod
    def sizeAll(event):
        for instance in Button.instances:
            instance.size()

    def command(self):
        if self.func:
            pass
        else:
            entry.configure(state='normal')
            entry.insert('end', self.text)
            entry.configure(state='readonly')

window = tkinter.Tk()
window.title('Kalkulacka')
window.bind('<Configure>', Button.sizeAll)

entry = tkinter.Entry(font='10', justify='right', state='readonly')
entry.grid(column=0, row=0, columnspan=4, sticky='WENS')

b9 = Button('9', 2, 2)
b8 = Button('8', 1, 2)
b7 = Button('7', 0, 2)
b6 = Button('6', 2, 3)
b5 = Button('5', 1, 3)
b4 = Button('4', 0, 3)
b3 = Button('3', 2, 4)
b2 = Button('2', 1, 4)
b1 = Button('1', 0, 4)
b0 = Button('0', 0, 5)
bComma = Button(',', 1, 5)
bEqual = Button('=', 2, 5)
bPlus = Button('+', 3, 2)
bMinus = Button('-', 3, 3, key='minus')
bMultiply = Button('*', 3, 4)
bDivide = Button('/', 3, 5)
bPow = Button('^', 0, 1)
bSqrt = Button('√', 1, 1, key='s')
bClear = Button('C', 2, 1, key='c')
bDelete = Button('<', 3, 1, key='BackSpace')

tkinter.mainloop()