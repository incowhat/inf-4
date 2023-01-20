from random import randrange

stlpcov, riadkov = map(int, input('Zadaj maticu MxN: ').split('x'))

def nacitaj(riadok, stlpec):
    matica = list()

    for x in range(riadok):
        x = list()
        for y in range(stlpec):
            x.append(randrange(100))
        matica.append(x)

    return matica

def vytlac(matica):
    for i in matica:
        for j in i:
            print(f'{j:3}', end=' ')
        print()
    print()

def sucet(m1, m2):
    matica = [[] for _ in range(riadkov)]

    for y in range(riadkov):
        for x in range(stlpcov):
            matica[y].append(m1[y][x] + m2[y][x])
    
    return matica

a = nacitaj(riadkov, stlpcov)
vytlac(a)
b = nacitaj(riadkov, stlpcov)
vytlac(b)

vytlac(sucet(a, b))