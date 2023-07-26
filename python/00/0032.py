l, m, n = map(int, open(0).read().split())
m += n // 25
n %= 25
l += m // 4
m %= 4
print(l % 10 + m + n)