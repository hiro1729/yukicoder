N = 300000
isprime = [True] * N
isprime[0] = isprime[1] = False
for i in range(2, int(N ** 0.5 + 1)):
    if not isprime[i]:
        continue
    for j in range(i * i, N, i):
        isprime[j] = False
k = int(input())
n = int(input())
p = []
h = []
for i in range(k, n + 1):
    if isprime[i]:
        p.append(i)
        h.append(i % 9)
max_ = 0
ans = 0
le = len(p)
tf = [False] * 9
r = 0
for l in range(le):
    while r < le and not tf[h[r]]:
        tf[h[r]] = True
        r += 1
    if r - l >= max_:
        max_ = r - l
        ans = p[l]
    tf[h[l]] = False
print(ans)