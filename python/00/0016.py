x, n = map(int, input().split())
a = list(map(int, input().split()))
mod = 1000003
ans = 0
for i in range(n):
	ans += pow(x, a[i], mod)
	ans %= mod
print(ans)