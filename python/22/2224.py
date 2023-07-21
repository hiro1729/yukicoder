s = input()
if s[0] == 'x':
	print((1 << 32) - int(s[1:]))
else:
	print(s)