with open('SÚ2 Úloha 2.txt', 'r') as file:
    skratky = {}
    for line in file.readlines():
        line = line.split()
        skratky[line[0]] = ' '.join(line[1:])

while True:
    try:
        print(skratky[input('Skratka: ').upper()])
    except KeyError:
        print('Nie je v liste')