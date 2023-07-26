k, n, f, *a = map(int, open(0).read().split())
s = k * n - sum(a)
print(-1 if s < 0 else s)