def zistiKelo(bankovka, suma):
    pocet = suma//bankovka
    suma %= bankovka

    if pocet != 0:
        print(('bankovky' if bankovka >= 5 else 'mince   '), f'{bankovka:>3}€: {pocet:>3} ks.')
    
    if suma == 0:
        return

    match bankovka:
        case 500: zistiKelo(200, suma)
        case 200: zistiKelo(100, suma)
        case 100: zistiKelo(50, suma)
        case 50: zistiKelo(20, suma)
        case 20: zistiKelo(10, suma)
        case 10: zistiKelo(5, suma)
        case 5: zistiKelo(2, suma)
        case _: zistiKelo(1, suma)

suma = int(input('zadaj sumu: '))
print(f'Suma {suma}€ sa da vyskladat z tychto eurobankoviek a eurominci:')
zistiKelo(500, suma)