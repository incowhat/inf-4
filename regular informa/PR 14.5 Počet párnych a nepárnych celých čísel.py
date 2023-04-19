with open('PR 14.5.1a parne_neparne.txt', 'r+') as file:
    pocet = {'nul': 0, 'parne': 0, 'neparne': 0}
    
    for line in file.readlines():
        line = int(line)
        if line == 0: pocet['nul'] += 1
        elif line%2 == 0: pocet['parne'] += 1
        else: pocet['neparne'] += 1

    output = f'V subore {file.name} je: {pocet["nul"]:3} nul,\n'
    output+= f'{pocet["parne"]:{len(file.name)+17}} parnych cisel,\n'
    output+= f'{pocet["neparne"]:{len(file.name)+17}} neparnych cisel.'

    print(output)
    file.write('\n' + output)