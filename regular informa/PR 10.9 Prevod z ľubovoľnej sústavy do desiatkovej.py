cisloStr = input('zadaj cislo v lubovolnej sustave: ')
sustava = int(input('zadaj radix sustavy cisla, v desiatkovej sustave: '))
if sustava > 36:
    print(f'nevyhovujuca sustava: {sustava}')
    exit()

cisloDesiatkova = int()

for i, cislo in enumerate(cisloStr[::-1]):
    try: 
        cisloDesiatkova +=  int(cislo)* sustava**i
    except ValueError:
        if 9 < ord(cislo)-87 < sustava:
            cisloDesiatkova +=  (ord(cislo)-87) * sustava**i
        else:
            print(f'cislica *{cislo}* v cisle mimo zvolenej sustavy')
            exit()

print(cisloDesiatkova)