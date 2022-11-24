import tkinter

c = tkinter.Canvas(width=450, height=500, bg='white')
c.grid(column=0, row=0, columnspan=3)

def parabola():
    pass
def vrchol():
    pass
def ohnisko():
    pass

l1, l2, l3 = (tkinter.Label(text=t) for t in ('x-ova sur. vrchola', 'y-ova sur. vrchola', '|vrchol, riad priamka|'))
l1, l2, l3 = (l.grid(column=0, row=i+1) for i, l in enumerate((l1, l2, l3)))

e1, e2, e3 = (tkinter.Entry() for _ in range(3))
e1, e2, e3 = (l.grid(column=1, row=i+1, rowspan=2) for i, l in enumerate((e1, e2, e3)))

b1, b2, b3 = (tkinter.Button(text=c.__name__, command=c) for c in (parabola, vrchol, ohnisko))
b1, b2, b3 = (l.grid(column=i, row=4) for i, l in enumerate((b1, b2, b3)))

tkinter.mainloop()