a = [[i, i+1, i+2] for i in range(1, 10, 3)]

for i in range(3):
    for j in range(3):
        print(f'{a[i][j]}', end=' ')
    print()