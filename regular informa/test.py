import tkinter

def funkcia():
    print('Nemaj stres Aji!!!!')
    ajka.configure(text='Okej, budem sa snazit')

    text = entry.get()
    print(text)
    entry.delete(0, 'end')

ajka = tkinter.Button(text='Neviem nic a mam stres', padx=8, pady=12, bg='#ff00ff', activebackground='#ab00ba', fg='gold', command=funkcia)
ajka.pack(padx=100, pady=30)

entry = tkinter.Entry()
entry.pack()

tkinter.mainloop()
