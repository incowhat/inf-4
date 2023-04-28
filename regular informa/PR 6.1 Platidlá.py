def zistiKelo(suma):
    print(f'Suma {suma}€ sa da vyskladat z tychto eurobankoviek a eurominci:')

    for hodnota in (500, 200, 100, 50, 20, 10, 5, 2, 1):
        pocet = suma//hodnota
        suma %= hodnota

        if pocet != 0:
            print(('bankovky' if hodnota >= 5 else 'mince   '), f'{hodnota:>3}€: {pocet:>3} ks.')
        
        if suma == 0:
            return
    

zistiKelo(int(input('zadaj sumu: ')))