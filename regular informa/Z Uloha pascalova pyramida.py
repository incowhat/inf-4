def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

komb = lambda n, k: int(fact(n)/(fact(k)*fact(n-k)))
poschodi = int(input('Pocet poschodi: '))
z = len(''.join([str(komb(poschodi-1, q)) for q in range(poschodi)]))


for i in range(poschodi):
    riadok = ''
    for j in range(i+1):
        riadok += str(komb(i, j)) + ' '
    print(f'{riadok:^{z*2}}')