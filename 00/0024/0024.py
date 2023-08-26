n = int(input())
ok = [True] * 10
for _ in range(n):
	a, b, c, d, s = input().split()
	a, b, c, d = map(int, [a, b, c, d])
	if s == "NO":
		ok[a] = False
		ok[b] = False
		ok[c] = False
		ok[d] = False
	else:
		for i in range(10):
			if i not in [a, b, c, d]:
				ok[i] = False
for i in range(10):
	if ok[i]:
		print(i)