def zistiKelo(bankovka, suma):
    pocet = suma//bankovka
    suma %= bankovka

    if pocet != 0:
        print(('bankovky' if bankovka >= 5 else 'mince   '), f'{bankovka:>3}€: {pocet:>3} ks.')
    
    if 0 < suma:
        if   bankovka == 500: zistiKelo(200, suma)
        elif bankovka == 200: zistiKelo(100, suma)
        elif bankovka == 100: zistiKelo( 50, suma)
        elif bankovka ==  50: zistiKelo( 20, suma)
        elif bankovka ==  20: zistiKelo( 10, suma)
        elif bankovka ==  10: zistiKelo(  5, suma)
        elif bankovka ==   5: zistiKelo(  2, suma)
        else: zistiKelo(1, suma)

suma = int(input('zadaj sumu: '))
print(f'Suma {suma}€ sa da vyskladat z tychto eurobankoviek a eurominci:')
zistiKelo(500, suma)