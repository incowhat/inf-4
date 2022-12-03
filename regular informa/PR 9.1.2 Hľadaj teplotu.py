from random import randint

print('Zaznamenané teploty:', ' '.join(map(str, teploty := [randint(25, 36) for _ in range(31)])), sep='\n')
# vyroby list teploty s cislami, vytlaci teploty

hladaj = int(input('Zadaj hladanu teplotu: '))

# try:
#     print(f'Teplota {hladaj}°C bola v mesiaci jul prvy krat zaznamenana na {teploty.index(hladaj)}. den.')
# except ValueError:
#     print('Teplota sa v mesiaci jul nevyskytla')

for i, t in enumerate(teploty):
    if hladaj == t:
        teploty.append(i)

if len(teploty) == 31:
    print('Teplota sa v mesiaci jul nevyskytla')
else:
    print(f'Teplota {hladaj}°C sa vyskytla v tieto dni: {" ".join(map(str, teploty[31:]))}')