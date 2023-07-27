from heapq import heappop, heappush
n = int(input())
c = int(input())
v = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
y = list(map(int, input().split()))
m = list(map(int, input().split()))
x = [[] for _ in range(n)]
for i in range(v):
    x[s[i] - 1].append((m[i], y[i], t[i] - 1))
q = [(0, 0, 0)]
tcs = [float("inf")] * n
mcs = [float("inf")] * n
while q:
    tc, mc, p = heappop(q)
    if p == n - 1:
        exit(print(tc))
    for i in x[p]:
        nt = tc + i[0]
        nm = mc + i[1]
        np = i[2]
        if mc + i[1] > c:
            continue
        if nt < tcs[np] or nm < mcs[np]:
            heappush(q, (nt, nm, np))
            tcs[p] = nt
            mcs[p] = nm
print(-1)