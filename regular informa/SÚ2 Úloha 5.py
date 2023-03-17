with open('SÚ2 Úloha 5.txt', 'r') as file:
    lines = [tuple(line.split()) for line in file.readlines()]
    lines = tuple(lines)

pocitace = {line[1]: [] for line in lines}
pocitace = dict(sorted(pocitace.items()))
for line in lines:
    pocitace[line[1]].append(line[2])

najviac = [[]]
for pc in pocitace:
    pc = [pc, *
          pocitace[pc]]

    if len(najviac[0]) < len(pc):
        najviac = []
    elif len(najviac[0]) > len(pc):
        continue
    najviac.append(pc)

print(najviac)