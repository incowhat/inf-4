def fib(n, a=0, b=1, i=1):
    if n >= i:
        print(f'{i:2}. {a:4}')
        fib(n, a=b, b=a+b, i=i+1)

fib(8)