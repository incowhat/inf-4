import tkinter

def entryEdit(func):
    def wrapper(*args):
        entryPast.configure(state='normal')
        entry.configure(state='normal')
        func(*args)
        entry.configure(state='readonly')
        entryPast.configure(state='readonly')
    return wrapper


class Button:
    instances: list = []

    def __init__(self, text: str, column: int, row: int, func=None, key=None):
        self.func = func
        self.text = text
        self.button = tkinter.Button(text=text, command=self.command, borderwidth=1,
                                     justify='center', fg='#e0e0e0', bg='#111111', relief='ridge',
                                     activebackground='#555555', activeforeground='#ffffff')
        self.button.grid(column=column, row=row, sticky="WENS")
        self.button.bind_all(f'<KeyPress-{key if key else text}>', lambda e: self.button.invoke())
        self.button.bind('<Enter>', self.hover)
        self.button.bind('<Leave>', self.hover)

        Button.instances.append(self)

    def hover(self, event):
        if str(event)[1:6] == 'Enter':
            self.button.configure(fg='#ffffff', bg='#2f2f2f')
        else:
            self.button.configure(fg='#e0e0e0', bg='#111111')

    @entryEdit
    def command(self):
        global newEq
        if newEq:
            entryPast.delete(0, 'end')
            if newEq != 'error':
                entryPast.insert(0, entry.get())
            
            if self.text in '0123456789()Ans' or newEq == 'error':
                clear()
        newEq = False
        
        if self.func:
            self.func()
        else:
            entry.insert('end', self.text)


@entryEdit
def equal():
    global ans, newEq
    newEq = True
    expression = entry.get()
    expression = expression.replace('Ans', str(ans))
    
    entryPast.delete(0, 'end')
    entryPast.insert(0, expression)
    entry.delete(0, 'end')

    expression = expression.replace('**', 'uzSomDalDoKodu^tak**tamNebudu')
    expression = expression.replace('^', '**')
    expression = root(expression) # odmocnina, vyrobena funkcia -> ± chaos

    try:
        c = eval(expression) #cela matika okrem odmocniny

        if isinstance(c, float) and c.is_integer():
            c = int(c)
        ans = c # ans memory sa nastavi

        if not isinstance(c, int | float):
            return clear()
    except Exception as error:
        c = type(error).__name__
        clear()
        entry.configure(state='normal') # clear to zmeni na readonly tak vratime spat na normal
        newEq = 'error'
        
    entry.insert(0, str(c))


# BLACKMAGIC NESNAZIT SA POCHOPIT!!!!
def root(strToRoot):
    if '√' not in strToRoot:
        return strToRoot

    for i, item in enumerate(strToRoot[::-1]):
        if item != '√': continue
        
        i = len(strToRoot) - i-1

        for j, left in enumerate(strToRoot[i if i==0 else i-1::-1]): # ide od odmocniny dolava
            if j == 0 and left == ')':
                memory = root(strToRoot[:i])
                strToRoot = [q for q in strToRoot]
                del strToRoot[:i]
                strToRoot.insert(0, eval(memory))
                strToRoot = ''.join(map(str, strToRoot))
                return root(strToRoot)
                    
            if left in '+-//**%()√':
                a = strToRoot[i-j:i]
                lt = i-j
                break
        else:
            a = strToRoot[:i]
            lt = 0
        if a == '':
            a = 2
            
        for j, right in enumerate(strToRoot[i+1:], 1):
            if j == 1 and right == '(':
                memory = root(strToRoot[i+1:])
                strToRoot = [q for q in strToRoot]
                del strToRoot[i+1:]
                strToRoot.append(eval(memory))
                strToRoot = ''.join(map(str, strToRoot))
                return root(strToRoot)

            if right in '+-//**%()√':
                b = strToRoot[i+1:i+j]
                rt = i+j
                break
        else:
            b = strToRoot[i+1:]
            rt = None

        try:
            oneRoot = pow(float(b), 1/float(a))
            strToRoot = [i for i in strToRoot]
            del strToRoot[lt:rt]
            strToRoot.insert(lt, str(oneRoot))
            strToRoot = ''.join(strToRoot)
        except Exception:
            strToRoot = '++' # syntax error ked to hodi do eval
        break
    return root(strToRoot)


@entryEdit
def delete():
    if entry.get()[-3:] == 'Ans':
        last = entry.index('end') - 3
    else:
        last = entry.index('end') - 1
    entry.delete(last, 'end')


@entryEdit
def clear(event=None):
    if event: return
    if entry.get() == '':
        entryPast.delete(0, 'end')    
    entry.delete(0, 'end')    


def resize(event):
    window.grid_columnconfigure('all', weight=1)
    window.grid_rowconfigure('all', weight=1)
    txtSize = 12 + (window.winfo_width()+window.winfo_height())//90

    for instance in Button.instances:
        if instance in (bAns, bDelete):
            instance.button.configure(font=('Consolas', int(txtSize * 0.6), 'bold'))
        else:
            instance.button.configure(font=('Consolas', txtSize))

    entry.configure(font=('Consolas', txtSize))
    entryPast.configure(font=('Consolas', txtSize))


window = tkinter.Tk()
window.title('Kalkulacka')
window.configure(bg='#111111')
window.bind('<Configure>', resize)

entryPast = tkinter.Entry(justify='right', state='readonly')
entryPast.configure(fg='grey', bg='green', relief='flat')
entryPast.grid(column=0, row=0, columnspan=4, sticky='WENS')

entry = tkinter.Entry(justify='right', state='readonly', fg='#ffffff', bg='#111111')
entry.grid(column=0, row=1, columnspan=4, sticky='WENS')
entry.bind_all('<Control-c>', clear) # ken nahodou niekto kopiruje aby sa nezmzal vysledok

ans = 'esteNieJe'
newEq = False

b0 = Button('0', 0, 7)
b1 = Button('1', 0, 6)
b2 = Button('2', 1, 6)
b3 = Button('3', 2, 6)
b4 = Button('4', 0, 5)
b5 = Button('5', 1, 5)
b6 = Button('6', 2, 5)
b7 = Button('7', 0, 4)
b8 = Button('8', 1, 4)
b9 = Button('9', 2, 4)
bBracketL = Button('(', 0, 2)
bBracketR = Button(')', 1, 2)
bClear = Button('C', 2, 2, key='c', func=clear)
bDelete = Button('⌫', 3, 2, key='BackSpace', func=delete)
bPowr = Button('^', 0, 3, key='p')
bNtroot = Button('√', 1, 3, key='s')
bModulo = Button('%', 2, 3)
bDivide = Button('/', 3, 3)
bMultiply = Button('*', 3, 4)
bMinus = Button('-', 3, 5, key='minus')
bPlus = Button('+', 3, 6)
bPoint = Button('.', 1, 7)
bAns = Button('Ans', 2, 7, key='a')
bEqual = Button('=', 3, 7, func=equal)

tkinter.mainloop()