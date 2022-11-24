a, b = list(map(int, [input(f'Zadaj {i} hranicu intervalu: ') for i in ['hornu', 'dolnu']]))

for i in range(a, b+1):
    print(i, end=' ')
