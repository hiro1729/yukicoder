def b(i, c):
	return chr(ord('A') + (ord(c) - ord('A') - i) % 26)
s = input()
print(''.join(b(i + 1, c) for i, c in enumerate(s)))