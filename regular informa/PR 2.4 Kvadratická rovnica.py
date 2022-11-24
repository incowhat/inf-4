a, b, c = list(map(int, [input(f'Zadaj cele cislo {i}: ') for i in ['a', 'b', 'c']]))

d = b**2-4*a*c
x1 = (-b+d**(1/2))/(2*a)

if d > 0:
    # vypocita x2 iba ked ho potrebuje
    x2 = (-b-d**(1/2))/(2*a)
    # \u... su dolne indexy cisel 1 a 2
    print(f'x\u2081 = {x1}\nx\u2082 = {x2}')
elif d == 0:
    print(f'odpoved je iba 1 realne cislo x = {x1}')
else:
    print('odpoved v obore realnych cisel neexisstuje')
