n_pocetNadob, q_pocetZmien = tuple(map(int, input().strip().rsplit(' ')))
a_chutNadobach = list(map(float, input().strip().rsplit(' ')))
p_b_zmeny = [tuple(map(float, input().strip().rsplit(' '))) for _ in range(q_pocetZmien)]

for zmena in p_b_zmeny:
    a_chutNadobach[int(zmena[0])-1] = zmena[1]
    # zmeni chut v nadobe

    average = lambda l: sum(l)/len(l)

    chutKornutku = (average(a_chutNadobach[0:k]) for k in range(1, n_pocetNadob+1))
    # chut kornutkov

    naj = [int(), float()]
    for i, ko in enumerate(chutKornutku):
        if ko > naj[1]:
            naj[0] = i+1
            naj[1] = ko

    print(str(naj[0]))