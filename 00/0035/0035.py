ok = 0
ng = 0
for _ in range(int(input())):
	t, s = input().split()
	t = int(t)
	l = len(s)
	c = 12 * t // 1000
	if l <= c:
		ok += l
	else:
		ok += c
		ng += l - c
print(ok, ng)