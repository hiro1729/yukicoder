n, p = map(int, input().split())
c = 0
while n:
	n //= p
	c += n
print(pow(p, c, 998244353))