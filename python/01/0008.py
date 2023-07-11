for _ in range(int(input())):
	n, k = map(int, input().split())
	n %= (k + 1)
	print("Lose" if n == 1 else "Win")