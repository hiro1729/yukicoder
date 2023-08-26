n = int(input())
m = int(input())
c = [1, 2, 3]
for _ in range(m):
	p, q = map(int, input().split())
	p -= 1
	q -= 1
	c[p], c[q] = c[q], c[p]
print(c.index(n) + 1)