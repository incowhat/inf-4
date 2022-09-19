a, b = list(map(int, [input(f'Zadaj cele cislo {i}: ') for i in ['a', 'b']]))

print(a, '+', b, '=', a+b, sep='')
print(a, '*', b, '=', a*b, sep='')
print(a, ':', b, '=', a/b, sep='')
print(a, ':', b, '=', a//b, ' zv. ', a%b, sep='')
print('aritmetický priemer', (a+b)/2)
