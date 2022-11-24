celkovo = int(input())
ciary = ''.join([input() for _ in range(celkovo)])

if (ciary.count('<')+ciary.count('>'))%2:
    print('had')
else:
    print('dazdovka')