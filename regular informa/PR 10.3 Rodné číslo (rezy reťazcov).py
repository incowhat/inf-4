try:
    rc = input('Rodne cislo: ').replace('/', '')
    if int(rc) % 11:
        raise ValueError

except ValueError: # ak bola zadana zla hodnota, alebo ina ako cisla
    print('Nepripustne rodne cislo')
    exit()

rc = list(rc)

def fromList(od:int, do:int, /, toint=False):
    _ = ''.join(rc[od:do+1])
    if toint:
        return int(_)
    return _

if int(fromList(2, 3)) > 50: # zmeni mesiac zeny spat na spravny mesiac, lebo 50
    pohlavie = 'zena'
    rc[2] = str(int(rc[2])-5)
else:
    pohlavie = 'muz'

if int(fromList(0, 1)) > 54: # prida rok, tisicky a stovky podla dvojcislia na rc
    rc.insert(0, '1'); rc.insert(1, '9')
else:
    rc.insert(0, '2'); rc.insert(1, '0')

print(f'Datum narodenia: {fromList(0, 3)}.{fromList(4, 5, toint=True)}.{fromList(6, 7, toint=True)}')
print(f'Pohlavie: {pohlavie}')