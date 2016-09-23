
def fib(n):
    if n < 3:
        return 1
    a, b, n = 1, 1, n-2
    for _ in range(n):
        a, b = a+b, a
    return a

result = fib({arg})
print(result)
