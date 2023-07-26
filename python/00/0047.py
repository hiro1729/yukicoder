from math import log2
n = int(input())
if n == 1:
	print(0)
else:
	print(int(log2(n - 1)) + 1)