n = int(input())
s = set(list(range(10)))
no = set()
for _ in range(n):
	l = input().split()
	t = set(map(int, l[:4]))
	if l[4] == "YES":
		s &= t
	else:
		no |= t
k = set()
for i in range(10):
	if i not in no:
		k.add(i)
s = list(s & k)
assert len(s) == 1
print(s[0])