n = int(input())
cnt = [0] * 10
for i in range(n):
	a, b, c = map(int, input().split())
	cnt[a - 1] += 1
	cnt[b - 1] += 1
	cnt[c - 1] += 1
s = 0
t = 0
for i in cnt:
	s += i // 2
	t += i % 2
print(s + t // 4)