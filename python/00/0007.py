n = int(input())
def EraSieve(n: int) -> list:
    r = [True] * (n + 1)
    r[0] = r[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if r[i]:
            for j in range(2 * i, n + 1, i):
                r[j] = False
    return r
p = [i for i, j in enumerate(EraSieve(n)) if j]
dp = [-1 for _ in range(n + 1)]
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
	k = 0
	for j in p:
		if j > i:
			break
		if dp[i - j] == 0:
			k = 1
			break
	dp[i] = k
print("Win" if dp[n] else "Lose")