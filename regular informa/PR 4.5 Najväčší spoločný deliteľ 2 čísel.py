from math import sqrt

a, b = list(map(int, [input(f'Zadaj cele kladne cislo {i}: ') for i in ['a', 'b']]))
delitelA, delitelB = [], []
max = lambda i: round(sqrt(i))

for i, nsd in [[a, delitelA], [b, delitelB]]:    
    for num in range(1, max(i)+1):
        if not i%num:
            nsd.append(num)
            nsd.append(int(i/num)) if num != max(i) else 0
            # prida opacny delitel ku delitelom po odmocninu, ak nie je duplikat
            # duplikat je iba ak ma cislo neparny pocet delitelov (napr. 64)

    nsd.sort()
    print(f'Delitele cisla {i}: ', nsd)

for j in delitelA:
    if j in delitelB:
        max = j
        # reuse premennej max na najvacsi spol delitel

print(f'Najvacsi spolocny delitel cisel {a} a {b} je: {max}')