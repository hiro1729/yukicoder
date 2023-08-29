x = int(input())
y = int(input())
l = int(input())
ans = (abs(x) + l - 1) // l + (abs(y) + l - 1) // l
if y >= 0 and x != 0:
	ans += 1
elif y < 0:
	ans += 2
print(ans)