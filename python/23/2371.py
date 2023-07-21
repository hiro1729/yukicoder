h, m = input().split()
s = h.zfill(2) + m.zfill(2) + "30"
if s < "073000":
	print("Yes")
elif s < "083000":
	print("Late")
else:
	print("No")