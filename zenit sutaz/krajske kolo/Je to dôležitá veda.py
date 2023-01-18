from random import randint

veci = [map(int, input().strip().rsplit(' ')) for _ in range(int(input()))]

for x, y, z in veci:
    print(randint(0, 3))
