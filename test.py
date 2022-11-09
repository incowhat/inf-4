import tkinter
from tkinter.colorchooser import askcolor

def savestep(event):
    global step
    step += 1
    # uloží aktuálny krok do tagu objektu na canvase

def stepback(event):
    global step
    canvas.delete(f's{step-1}')
    if 0 < step:
        step -= 1
    # zmaže posledný vytvorený objekt, alebo skupinu objektov, krok späť

def cursor(event, delete=None):
    global x1, y1
    canvas.delete('cursor')
    x = event.x
    y = event.y
    x1, y1 = x, y
    if selected == ceruza or selected == dúhová_ceruza or delete != None:
        canvas.create_oval(x-halfsize,y-halfsize,x+halfsize,y+halfsize, outline = '#6104B4', width = 2, tags = 'cursor')
    else:
        selected(x, y, x1, y1, 'cursor', color)
    # tvorí vlastný kurzor na canvase alebo maketu zvoleného nástroja

def draw(event):
    x = event.x
    y = event.y
    selected(x, y, x1, y1, f's{step}', color)
    cursor(event)
    # zabezpečuje kreslenie na canvas

def draw2(event):
    x = event.x
    y = event.y
    ceruza(x, y, x1, y1, f's{step}', color2)
    cursor(event, True)
    # kreslenie na canvas sekundárnou farbou

def changesize(event):
    global size, halfsize
    if 4.5 < size * (1.001 ** event.delta) < 1000:
        size *= 1.001 ** event.delta
        halfsize = size/2
        cursor(event, True)
    # mení veľkosť kurzora, a niektorých nástrojov

def select(event):
    global selected
    selected = eval(menusel.get())
    # zabezpečuje zmenu zvoleného nástroja

def selcer():
    menusel.set(Nastroje[0])
    select(1)
    # rýchle zvolenie nástroja ceruza

# \/ \/ \/ \/ definície jednotlivých nástrojov
def ceruza(x, y, x1, y1, tag, color):
    canvas.create_oval(x-halfsize,y-halfsize,x+halfsize,y+halfsize, fill = color, outline = '', tags = tag)
    canvas.create_line(x1, y1, x, y, width = size, fill = color, tags = tag)

def dúhová_ceruza(x, y, x1, y1, tag, color):
    global duhacolor, duhahex
    duhahex = '#%02x%02x%02x' % (duhacolor['r'],duhacolor['g'],duhacolor['b'])
    canvas.create_oval(x-halfsize,y-halfsize,x+halfsize,y+halfsize, fill = duhahex, outline = '', tags = tag)
    canvas.create_line(x1, y1, x, y, width = size, fill = duhahex, tags = tag)
    if duhacolor['r'] == 255 and duhacolor['g'] < 256-duhaspeed and duhacolor['b'] == 0:
        duhacolor['g'] += duhaspeed
    if duhaspeed-1 < duhacolor['r'] and duhacolor['g'] == 255 and duhacolor['b'] == 0:
        duhacolor['r'] -= duhaspeed
    if duhacolor['g'] == 255 and duhacolor['b'] < 256-duhaspeed and duhacolor['r'] == 0:
        duhacolor['b'] += duhaspeed
    if duhaspeed-1 < duhacolor['g'] and duhacolor['b'] == 255 and duhacolor['r'] == 0:
        duhacolor['g'] -= duhaspeed
    if duhacolor['b'] == 255 and duhacolor['r'] < 256-duhaspeed and duhacolor['g'] == 0:
        duhacolor['r'] += duhaspeed
    if duhaspeed-1 < duhacolor['b'] and duhacolor['r'] == 255 and duhacolor['g'] == 0:
        duhacolor['b'] -= duhaspeed

def Japonská_vlajka(x,y,x1,y1,tag,color):
    canvas.create_rectangle(x, y, x+300, y+200, fill='white', tags=tag)
    canvas.create_oval(x+70, y+25, x+230, y+175, fill='red', tags=tag)
    # Lukaa
def smutný_smajlík(x,y,x1,y1,tag,color):
    canvas.create_oval(x,y,x+22,y+22, fill='yellow', tags=tag)
    canvas.create_oval(x+4,y+5,x+9,y+10, fill= color, tags=tag)
    canvas.create_oval(x+14,y+5,x+19,y+10, fill= color, tags=tag)
    canvas.create_text(x+14,y+16,text='(',angle=270, tags=tag)
    # Lukaa
def značka_7t(x,y,x1,y1,tag,color):
    canvas.create_oval(x, y, x+180, y+170, fill='red', tags=tag)
    canvas.create_oval(x+10, y+10, x+170, y+160, fill='white', tags=tag)
    canvas.create_text(x+90, y+85, text='7 t', fill='black', font='Arial 40 bold', tags=tag)
    # Lukaa
def vlajka_Bangladéš(x,y,x1,y1,tag,color):
    canvas.create_rectangle(x, y, x+280, y+200, fill='dark green', tags=tag)
    canvas.create_oval(x+45, y+20, x+205, y+170, fill='red', tags=tag)
    # Lukaa
def kruh(x,y,x1,y1,tag,color):
    canvas.create_oval(x,y,x1+size*1.2,y+size*1.2, outline= color, width='10', fill='red', tags=tag)
    # Lukaa
def trojuholník(x,y,x1,y1,tag,color):
    canvas.create_line(x+10,y,x-90,y+190,x+110,y+190,x+10,y, fill= color, tags=tag)
    # Lukaa

def robot(x,y,x1,y1,tag,color):
    canvas.create_rectangle(x, y, x+60, y+100, fill='gray', tags = tag)
    canvas.create_rectangle(x+10, y+20,x+50,y+80,fill='slategray', tags = tag)
    canvas.create_oval(x+30,y+40,x+40,y+50,fill='indianred', tags = tag)
    canvas.create_rectangle(x+10, y-50, x+50, y-10, fill='gray', tags = tag)
    canvas.create_rectangle(x+20,y,x+40,y-10,fill='firebrick', tags = tag)
    canvas.create_line(x+20,y-5,x+40,y-5, tags = tag)
    canvas.create_rectangle(x+25,y-50,x+35,y-70,fill='firebrick', tags = tag)
    canvas.create_oval(x+20,y-55,x+40,y-75,fill='cyan',outline='dodgerblue', tags = tag)
    canvas.create_oval(x+15, y-40, x+25, y-30, fill='yellow', tags = tag)
    canvas.create_oval(x+35, y-40, x+45, y-30, fill='yellow', tags = tag)
    canvas.create_oval(x+20, y-35, x+25, y-30, fill='red',outline='red', tags = tag)
    canvas.create_oval(x+40, y-35, x+45, y-30, fill='red',outline='red', tags = tag)
    canvas.create_rectangle(x+15, y-20, x+45, y-15, fill='firebrick', tags = tag)
    canvas.create_line(x+20,y-20,x+20,y-15, tags = tag)
    canvas.create_line(x+25,y-20,x+25,y-15, tags = tag)
    canvas.create_line(x+30,y-20,x+30,y-15, tags = tag)
    canvas.create_line(x+35,y-20,x+35,y-15, tags = tag)
    canvas.create_line(x+40,y-20,x+40,y-15, tags = tag)
    canvas.create_rectangle(x+5, y+100, x+25, y+180, fill='firebrick', tags = tag)
    canvas.create_rectangle(x+35, y+100, x+55, y+180, fill='firebrick', tags = tag)
    canvas.create_rectangle(x,y+160,x+30,y+180,fill='gray', tags = tag)
    canvas.create_rectangle(x+30,y+160,x+60,y+180,fill='gray', tags = tag)
    canvas.create_line(x+5,y+120,x+25,y+120, tags = tag)
    canvas.create_line(x+5,y+140,x+25,y+140, tags = tag)
    canvas.create_line(x+5,y+160,x+25,y+160, tags = tag)
    canvas.create_line(x+35,y+140,x+55,y+140, tags = tag)
    canvas.create_line(x+35,y+160,x+55,y+160, tags = tag)
    canvas.create_line(x+35,y+120,x+55,y+120, tags = tag)
    canvas.create_line(x, y+10, x-40, y+50, width=15, tags = tag)
    canvas.create_line(x+60, y+10, x+110, y+55, width=15, tags = tag)
    # Mateej

def smajlík(x,y,x1,y1,tag,color):
    canvas.create_oval(x,y,x+22,y+22, fill='yellow', tags=tag)
    canvas.create_oval(x+4,y+5,x+9,y+10, fill='white', tags= tag)
    canvas.create_oval(x+14,y+5,x+19,y+10, fill='white', tags=tag)
    canvas.create_text(x+14,y+16,text=')', angle=270, tags=tag)
    # Tomaaš
def značka_nemocnica(x,y,x1,y1,tag,color):
    canvas.create_rectangle(x, y, x+180, y+170, fill='navyblue', tags=tag)
    canvas.create_text(x+90, y+70, text='H', fill='white', font='Arial 130 bold', tags=tag)
    canvas.create_text(x+90, y+150, text='NEMOCNICA', fill='white', font='Arial 20 bold', tags=tag)
    # Tomaaš
def ovály(x,y,x1,y1,tag,color):
    canvas.create_oval(x,y,x1+2.2,y1+size*2.2, fill='yellow', tags=tag)
    # Tomaaš
def štvorec(x,y,x1,y1,tag,color):
    canvas.create_rectangle(x,y,x1+size*1.2,y1+size*1.2, tags=tag)
    # Tomaaš
def vlajka_Tonga(x,y,x1,y1,tag,color):
    canvas.create_rectangle(x, y, x+300, y+200, fill='red', tags=tag)
    canvas.create_rectangle(x, y, x+150, y+120, fill='white', tags=tag)
    canvas.create_text(x+75,y+60, text='+', font='Arial 100', fill='red', tags=tag)
    # Tomaaš
def vlajka_Švajčiar(x,y,x1,y1,tag,color):
    canvas.create_rectangle(x, y, x+300, y+200, fill='red', tags=tag)
    canvas.create_text(x+150,y+100, text='+', font='Arial 200', fill='white', tags=tag)
    # Tomaaš
# /\ /\ /\ /\ definície jednotlivých nástrojov

Nastroje = [
    'ceruza', 'dúhová_ceruza', 'Japonská_vlajka', 'smutný_smajlík', 'značka_7t', 'vlajka_Bangladéš', 'kruh', 'trojuholník',
    'robot', 'smajlík', 'značka_nemocnica', 'ovály', 'štvorec', 'vlajka_Tonga', 'vlajka_Švajčiar'
] # list výberu nástrojov

def col1indicator(col):
    gui.create_text(410, 30, text = 'farba 1', font = 'Consolas 11')
    gui.create_rectangle(390, 40, 430, 80, fill = col)

def col2indicator(col):
    gui.create_text(490, 30, text = 'farba 2', font = 'Consolas 11')
    gui.create_rectangle(470, 40, 510, 80, fill = col)

class Tlacidlo:
    # class pre rýchle vytvorenie tlačidiel na zmenu farby
    def __init__(self, bcolor, sticky, padx, pady):
        self.bcolor = bcolor
        self.sticky = sticky
        self.padx   = padx
        self.pady   = pady
        self.button = tkinter.Button(command = self.changebcolor, default = 'normal', padx = 8, relief = 'groove', cursor = 'hand2', bg = self.bcolor, activebackground = self.bcolor)
        self.button.grid(row = 0, column = 0, sticky = sticky, padx = padx+20, pady = pady)
        self.button.bind('<3>', self.changebutton)
        self.button.bind('<2>', self.changebg)
        # inicializačné príkazy pre vytváranie inštancie tohto classu (vytvorí tlačidlo)

    def changebutton(self, event):
        global color
        self.bcolor = askcolor()[1]
        color = self.bcolor
        self.button.configure(command = self.changebcolor, bg = self.bcolor, activebackground = self.bcolor)
        # zmena farby tlačidla pomocou pravého tlačidla myši

    def changebcolor(self):
        global color
        color = self.bcolor
        col1indicator(color)
        # zmení globálnu premennú color zodpovednú za farbu niektorých nástrojov

    def changebg(self, event):
        global color2
        canvas.delete('all')
        canvas['bg'] = self.bcolor
        color2 = canvas['bg']
        col2indicator(color2)
        # zmena farby pozadia a vymazanie canvasu naraz

tkinter.Tk().title('GTA paint')
# názov programu
gui = tkinter.Canvas(width=1000, height = 100, bg = 'lightgray')
gui.grid(row = 0, column = 0)
col1indicator('black')
col2indicator('white')
# plocha možností
menucv = tkinter.Canvas(width=0, height = 0)
menucv.grid(row = 0, column = 0, sticky = 'E', padx = 90)
# výber nástroja
zahadnamedzera = tkinter.Canvas(height = 20)
zahadnamedzera.grid(row = 1, column = 0)
# prázdne miesto pod možnosťami
canvas = tkinter.Canvas(width=940, height = 500, bg = 'white')
canvas.grid(row = 2, column = 0)
canvas.config(cursor = 'none')
# plocha na kreslenie
poslednenic = tkinter.Canvas(width = 1000, height = 20)
poslednenic.grid(row = 3, column = 0)
poslednenic.create_text(100, 10, text = 'Oliver, Tomáš, Matej, Luka', font = 'Consolas 10', fill = 'gray')
poslednenic.create_text(894, 10, text = '© 2021 všetky práva vyhradené', font = 'Consolas 10', fill = 'gray')
# prázdne miesto na spodku obrazovky

# \/ vytvorenie tlačidiel na zmeny farby pomocou classu Tlacidlo
b1  = Tlacidlo('black', 'NW', 25, 10)
b2  = Tlacidlo('gray', 'NW', 55, 10)
b3  = Tlacidlo('brown', 'NW', 85, 10)
b4  = Tlacidlo('red', 'NW', 115, 10)
b5  = Tlacidlo('orange', 'NW', 145, 10)
b6  = Tlacidlo('yellow', 'NW', 175, 10)
b7  = Tlacidlo('green', 'NW', 205, 10)
b8  = Tlacidlo('deepskyblue','NW',235,10)
b9  = Tlacidlo('blue','NW',265,10)
b10 = Tlacidlo('purple','NW',295,10)
b11 = Tlacidlo('snow','NW',25,40)
b12 = Tlacidlo('gainsboro','NW',55,40)
b13 = Tlacidlo('peru','NW',85,40)
b14 = Tlacidlo('lightpink','NW',115,40)
b15 = Tlacidlo('gold','NW',145,40)
b16 = Tlacidlo('lemonchiffon','NW',175,40)
b17 = Tlacidlo('lime','NW',205,40)
b18 = Tlacidlo('paleturquoise','NW',235,40)
b19 = Tlacidlo('lightsteelblue','NW',265,40)
b20 = Tlacidlo('magenta','NW',295,40)
b21 = Tlacidlo('white','SW',25, 10)
b22 = Tlacidlo('white','SW',55, 10)
b23 = Tlacidlo('white','SW',85, 10)
b24 = Tlacidlo('white','SW',115,10)
b25 = Tlacidlo('white','SW',145,10)
b26 = Tlacidlo('white','SW',175,10)
b27 = Tlacidlo('white','SW',205,10)
b28 = Tlacidlo('white','SW',235,10)
b29 = Tlacidlo('white','SW',265,10)
b30 = Tlacidlo('white','SW',295,10)
# Mateej
# /\ vytvorenie tlačidiel na zmeny farby pomocou classu Tlacidlo

# \/ vytvorenie premenných, ktoré sú potrebné na chod aplikácie
selected = ceruza
step = 1
size = 10
halfsize = size/2
color = 'black'
color2 = canvas['bg']
duhacolor = {'r':255, 'g':0, 'b':0}
duhaspeed = 5
menusel = tkinter.StringVar()
menusel.set(Nastroje[0])
# /\ vytvorenie premenných, ktoré sú potrebné na chod aplikácie

nastrojmenu = tkinter.OptionMenu(menucv, menusel, *Nastroje, command = select)
nastrojmenu.grid(row = 0, column = 0)
nastrojmenu.config(cursor = 'hand2', font = 'Consolas 17', borderwidth = 0)
buttonceruza = tkinter.Button(command = selcer, text = '!', font = 'Wingdings 16', relief = 'groove')
buttonceruza.grid(row = 0, column = 0, sticky = 'E', padx = 33)
# vytvorenie menu na zvolenie nástroja

canvas.bind('<Motion>', cursor)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<1>', draw)
canvas.bind('<B1-ButtonRelease>', savestep)
canvas.bind('<B3-Motion>', draw2)
canvas.bind('<3>', draw2)
canvas.bind('<B3-ButtonRelease>', savestep)
canvas.bind_all('<Control-z>', stepback)
canvas.bind('<MouseWheel>', changesize)
# využitie príkazu bind pre rôzne funkcie

tkinter.mainloop()