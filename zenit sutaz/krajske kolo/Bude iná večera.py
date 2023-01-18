from random import shuffle

if (c := int(input())) == 1:
    input()
    print('Janka bude frflat')
    exit()
    
jedla = list(input().rsplit(' '))
if len(jedla) == jedla.count(jedla[0]):
    print('Janka bude frflat')
elif jedla[::-1] != jedla:
    print(' '.join(jedla[::-1]))
else:
    while True:
        rnd = list(jedla)
        shuffle(rnd)

        if rnd != jedla:
            print(' '.join(rnd))
            exit()