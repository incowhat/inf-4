a, b, c, x, y = list(map(int, [input(f'Zadaj cele cislo {i}: ') for i in ['a', 'b', 'c', 'x', 'y']]))

print('bod [{}, {}] {}lezi na priamke p: '.format(x, y, 'ne' if (a*x)+(b*y)+c else ''), a, 'x + ', b, 'y + ', c, ' = 0', sep='') 