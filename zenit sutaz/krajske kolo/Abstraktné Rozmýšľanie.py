def f(x):
    if x == 0:
        return 1

    return (f(x-1)*2) % 47

n = int(input())

for i in range(1,n+1):
    candy = 0
    for j in range(1,n+1):
        if j == n and i % 2:
            break
        elif not (i % j):
            candy = candy + int(chr(49)+chr(48),2)
    else: continue

    if candy == 1:
        res = f(n-i)
        print(res)
    elif not (candy and (candy | 3 == candy + 3)):
        print(i)