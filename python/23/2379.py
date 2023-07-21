def factorize(n: int) -> list:
    r = []
    for p in range(2, int(n ** 0.5) + 1):
        if n % p != 0:
            continue
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        r.append((p, e))
    if n != 1:
        r.append((n, 1))
    return r

p = factorize(int(input()))
print("Yes" if len(p) <= 2 else "No")