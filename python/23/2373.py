n = int(input())
s = input()
def match(s, p):
	for s, p in zip(s, p):
		if s != p and s != '?':
			return False
	return True
dp = [False] * (n + 1)
dp[0] = True
for i in range(n):
	if dp[i]:
		for p in ["wa", "wo", "n"]:
			if i + len(p) <= n and match(s[i: i + len(p)], p):
				dp[i + len(p)] = True
print("Yes" if dp[n] else "No")