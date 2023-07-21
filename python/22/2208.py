for _ in range(int(input())):
	l, r, a, b = map(int, input().split())
	print(max(l * a + b, r * a + b))