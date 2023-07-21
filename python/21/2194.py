a, b, c = map(int, input().split())
t = False
if c % a == 0:
	n = c // a
	if n * a <= b:
		print(n)
		t = True
if (b + c) % a == 0:
	n = (b + c) // a
	if n * a > b:
		print(n)
		t = True
if not t:
	print(-1)