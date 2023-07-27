from collections import deque
n = int(input())
d = [0] * (n + 1)
d[1] = 1
q = deque()
q.append(1)
while q:
	v = q.popleft()
	if v == n:
		exit(print(d[v]))
	b = v.bit_count()
	a = v + b
	c = v - b
	if a <= n and d[a] == 0:
		d[a] = d[v] + 1
		q.append(a)
	if c > 0 and d[c] == 0:
		d[c] = d[v] + 1
		q.append(c)
print(-1)