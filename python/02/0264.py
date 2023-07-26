n, k = map(int, input().split())
if n == k:
	print("Drew")
elif (n == 1 and k == 0) or (n == 0 and k == 2) or (n == 2 and k == 1):
	print("Lost")
else:
	print("Won")