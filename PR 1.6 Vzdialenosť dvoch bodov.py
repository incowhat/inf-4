from math import sqrt

ax, ay, bx, by = list(map(int, [input(f'{i} = ') for i in ['Ax', 'Ay', 'Bx', 'By']]))

vzd = round(sqrt((bx-ax)**2 + (by-ay)**2), 2)
print(f'Vzdialenost bodov A[{ax}, {ay}] a A[{bx}, {by}] je {vzd})
