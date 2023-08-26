l = int(input())
n = int(input())
w = list(map(int, input().split()))
w.sort()
ans = 0
s = 0
for i in range(n):
	s += w[i]
	if s <= l:
		ans += 1
		continue
	break
print(ans)