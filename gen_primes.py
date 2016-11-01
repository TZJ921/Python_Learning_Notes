def gen_primes():
    n = 2
    primes = set()
    while True:
        for i in primes:
            if n % i == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1

g = gen_primes()
print(next(g))
print(next(g))
