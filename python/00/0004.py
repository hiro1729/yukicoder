n = int(input())
w = list(map(int, input().split()))
o = 1
for i in w:
	o |= o << i
q, r = divmod(sum(w), 2)
print("impossible" if r == 1 or not ((o >> q) & 1) else "possible")