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
                                     justify='center', fg='#dedede', bg='#0f0f0f', relief='ridge',
                                     activebackground='#1a1a1a', activeforeground='#f0a059')
        self.button.grid(column=column, row=row, sticky="WENS")
        self.button.bind_all(f'<KeyPress-{key if key else text}>', lambda _: self.button.invoke())
        self.button.bind('<Enter>', self.hover)
        self.button.bind('<Leave>', self.hover)

        Button.instances.append(self)

    def hover(self, event):
        if str(event)[1:6] == 'Enter':
            self.button.configure(fg='#ffeeaa', bg='#222222')
        else:
            self.button.configure(fg='#dedede', bg='#0f0f0f')

    @entryEdit
    def command(self):
        global newEq
        if newEq:
            entryPast.delete(0, 'end')
            if newEq != 'error':
                entryPast.insert(0, entry.get())
            if self.text in '0123456789√()Ans' or newEq == 'error':
                clear()
                entry.configure(state='normal', fg='#f0f0f0')  # lebo clear zmeni state na readonly
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

    expression = expression.replace('**', 'uzSomDalDoKodu^tak**tamNebudu')  # urobi syntax error
    expression = expression.replace('()', 'ziadneHacksNebudu') # v eval sa snazilo sa odvolat objekt
    expression = expression.replace('^', '**')
    expression = clearCallableSyntaxWarnings(expression)
    try:
        expression = root(expression)  # odmocnina, vyrobena funkcia -> ± chaos
    except Exception:
        exp = '++'

    try:
        c = eval(expression)  #cela matika okrem odmocniny

        if isinstance(c, float) and c.is_integer():
            c = int(c)
        ans = c # ans memory sa nastavi

        if not isinstance(c, int | float):
            return clear()
        entry.insert(0, str(c))

    except Exception as error:
        c = type(error).__name__
        clear()   # \/ clear to zmenil na readonly tak vratime spat na normal
        entry.configure(state='normal', fg='#ee1111')  # cervena farba lebo error
        entry.insert(0, str(c))
        newEq = 'error'


# BLACKMAGIC CHAOS NESNAZIT SA POCHOPIT!!!!
# hodi error pri neparnej odmocnine zo zaporneho cisla
def root(exp):
    if '√' not in exp:
        return exp
    for i, item in enumerate(exp[::-1]):
        if item != '√':
            continue
        i = len(exp) - i-1

        for j, left in enumerate(exp[i if i==0 else i-1::-1]): # ide od odmocniny dolava
            if j == 0 and left == ')':  # zatvorky... chaos, ale ide
                close = j+2
                counter = 0
                while True:
                    if exp[i-close] == '(' and counter == 0: break
                    if exp[i-close] == '(': counter -= 1
                    if exp[i-close] == ')': counter += 1
                    close += 1
                memory = root(exp[i-close:i])
                exp = [q for q in exp]
                del exp[i-close:i]
                exp.insert(i-close, eval(memory))
                exp = ''.join(map(str, exp))
                return root(exp)
                    
            if left in '+-//**%()√':
                a = exp[i-j:i]
                lt = i-j
                break
        else:
            a = exp[:i]
            lt = 0
        if a == '':
            a = 2

        for j, right in enumerate(exp[i+1:], 1):
            if j == 1 and right == '(':  # tiez zatvorky
                close = j+1
                counter = 0
                while True:
                    if exp[i+close] == ')' and counter == 0: break
                    if exp[i+close] == ')': counter -= 1
                    if exp[i+close] == '(': counter += 1
                    close += 1
                memory = root(exp[i+1:i+close+1])
                exp = [q for q in exp]
                del exp[i+1:i+close+1]
                exp.insert(i+j, eval(memory))
                exp = ''.join(map(str, exp))
                return root(exp)

            if right in '+-//*%()√':
                b = exp[i+1:i+j]
                rt = i+j
                break
        else:
            b = exp[i+1:]
            rt = None

        oneRoot = pow(float(b), 1/float(a))
        exp = [i for i in exp]
        del exp[lt:rt]
        exp.insert(lt, str(oneRoot))
        exp = ''.join(exp)
    # syntax error ked to hodi do eval
    return exp


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

def clearCallableSyntaxWarnings(exp):
    if '(' not in exp:
        return exp
    
    for i, ch in enumerate(exp[1:], 1):
        if ch != '(':
            continue
        if exp[i-1] in '+-//**%(√':
            return exp
    return '0totoNieJeCallable'

def resize():
    window.grid_columnconfigure('all', weight=1)
    window.grid_rowconfigure('all', weight=1)
    txtSize = 12 + (window.winfo_width()+window.winfo_height())//90

    for instance in Button.instances:
        if instance.text in 'Ans⌫':
            instance.button.configure(font=('Consolas', int(txtSize * 0.6), 'bold'))
        else:
            instance.button.configure(font=('Consolas', txtSize))

    entry.configure(font=('Consolas', txtSize))
    entryPast.configure(font=('Consolas', txtSize))


window = tkinter.Tk()
window.title('Kalkulacka')
window.configure(bg='#111111')
window.bind('<Configure>', lambda _: resize())
window.bind('<Return>', lambda _: equal())  # aj = aj enter robia to iste

entryPast = tkinter.Entry(justify='right', state='readonly', fg='#00a020',
                          relief='flat', readonlybackground='#050505')
entryPast.grid(column=0, row=0, columnspan=4, sticky='WENS')

entry = tkinter.Entry(justify='right', state='readonly', fg='#f0f0f0',
                      relief='flat', readonlybackground='#050505')
entry.grid(column=0, row=1, columnspan=4, sticky='WENS')
entry.bind_all('<Control-c>', clear)  # ken nahodou niekto kopiruje aby sa nezmzal vysledok

ans = 'esteNieJe'
newEq = False

Button('0', 0, 7)
Button('1', 0, 6)
Button('2', 1, 6)
Button('3', 2, 6)
Button('4', 0, 5)
Button('5', 1, 5)
Button('6', 2, 5)
Button('7', 0, 4)
Button('8', 1, 4)
Button('9', 2, 4)
Button('(', 0, 2)
Button(')', 1, 2)
Button('C', 2, 2, key='c', func=clear)
Button('⌫', 3, 2, key='BackSpace', func=delete)
Button('^', 0, 3, key='p')
Button('√', 1, 3, key='r')
Button('%', 2, 3)
Button('/', 3, 3)
Button('*', 3, 4)
Button('-', 3, 5, key='minus')
Button('+', 3, 6)
Button('.', 1, 7)
Button('Ans', 2, 7, key='a')
Button('=', 3, 7, func=equal)

tkinter.mainloop()
