W, H, C = input().split()
W = int(W)
H = int(H)
row1 = ""
row2 = ""
if C == "B":
	for i in range(W):
		if i % 2 == 0:
			row1 += "B"
		else:
			row1 += "W"
	for i in range(W):
		if i % 2 == 0:
			row2 += "W"
		else:
			row2 += "B"
else:
	for i in range(W):
		if i % 2 == 0:
			row1 += "W"
		else:
			row1 += "B"
	for i in range(W):
		if i % 2 == 0:
			row2 += "B"
		else:
			row2 += "W"
for i in range(H):
	if i % 2 == 0:
		print(row1)
	else:
		print(row2)