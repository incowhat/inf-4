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
        entryPast.configure(font=('Calibri', txtSize))

    @staticmethod
    def sizeAll(event):
        for instance in Button.instances:
            instance.size()

    def command(self):
        if self.func:
            self.func()
        else:
            entry.configure(state='normal')
            entry.insert('end', self.text)
            entry.configure(state='readonly')

def entryEdit(func):
    def wrapper():
        entryPast.configure(state='normal')
        entry.configure(state='normal')
        func()
        entry.configure(state='readonly')
        entryPast.configure(state='readonly')
    return wrapper

    

@entryEdit
def equal():
    expression = entry.get()

    entryPast.delete(0, 'end')
    entryPast.insert(0, expression)
    entry.delete(0, 'end')

    expression = expression.replace('^', ' | Infix(lambda a, b: pow(a, b)) | ')
    print(expression)

    entry.insert(0, eval(expression))

@entryEdit
def delete():
    entry.delete(entry.index('end') - 1)

@entryEdit
def clear():
    entry.delete(0, 'end')




window = tkinter.Tk()
window.title('Kalkulacka')
window.bind('<Configure>', Button.sizeAll)

entryPast = tkinter.Entry(font='10', justify='right', state='readonly')
entryPast.configure(fg='grey', relief='flat')
entryPast.grid(column=0, row=0, columnspan=4, sticky='WENS')
entry = tkinter.Entry(font='10', justify='right', state='readonly')
entry.grid(column=0, row=1, columnspan=4, sticky='WENS')


b9 = Button('9', 2, 3)
b8 = Button('8', 1, 3)
b7 = Button('7', 0, 3)
b6 = Button('6', 2, 4)
b5 = Button('5', 1, 4)
b4 = Button('4', 0, 4)
b3 = Button('3', 2, 5)
b2 = Button('2', 1, 5)
b1 = Button('1', 0, 5)
b0 = Button('0', 0, 6)
bPoint = Button('.', 1, 6)
bEqual = Button('=', 3, 6, func=equal)
bPlus = Button('+', 3, 3)
bMinus = Button('-', 3, 4, key='minus')
bMultiply = Button('*', 2, 2)
bDivide = Button('/', 3, 2)
bPow = Button('^', 0, 2, key='p')
bSqrt = Button('√', 1, 2, key='s')
bClear = Button('C', 3, 5, key='c', func=clear)
bDelete = Button('<', 2, 6, key='BackSpace', func=delete)

tkinter.mainloop()