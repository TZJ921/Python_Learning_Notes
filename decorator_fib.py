def cache(fib):
    c = {}
    def wrapper(n):
        r = c.get(n)
        if r is None:
            r = c[n] = fib(n)
        return r
    return wrapper

@cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n-2) + fib(n-1)

print(fib(25))
