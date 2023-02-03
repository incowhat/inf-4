import tkinter

subor = 'PR 14.4 uspory.txt'

def hladaj():
    hlada = entry.get()
    vyskyt = []

    with open(subor, 'r') as file:
        for i, line in enumerate(file.readlines(), 1):
            if int(line) == int(hlada):
                vyskyt.append(str(i))

        if vyskyt:
            print(f'Vklad {hlada} sa na vypise vyskytol na', end='')
            for i, hodnota in enumerate(vyskyt, 1):
                print(f' {hodnota}.', end='')
                print(' a', end='') if i+1 == len(vyskyt) else (print(' den') if i == len(vyskyt) else print(',', end=''))
        else:
            print(f'Vklad {hlada} sa na vypise nevyskytol')
            

def vypis():
    with open(subor, 'r') as file:
        for i, line in enumerate(file.readlines(), 1):
            print(f'{i:3}. mesiac {int(line):3} eur')
            

label = tkinter.Label(text='Hodnota')
label.grid(column=0, row=0)
entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)

b1 = tkinter.Button(text='Hladaj hodnotu', command=hladaj, width=20)
b1.grid(column=0, row=1, columnspan=2)
b2 = tkinter.Button(text='Vypis uctu', command=vypis, width=20)
b2.grid(column=0, row=2, columnspan=2)

tkinter.mainloop()