from collections import Counter
N = int(input())
L = list(map(int, input().split()))
c = Counter(L)
max_cnt = 0
ans = -1
for i, j in list(c.items()):
	if j > max_cnt:
		max_cnt = j
		ans = i
	elif j == max_cnt and i > ans:
		ans = i
print(ans)