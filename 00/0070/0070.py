ans = 0
for _ in range(int(input())):
	s, e = input().split()
	sh, sm = map(int, s.split(':'))
	eh, em = map(int, e.split(':'))
	t = eh * 60 + em - (sh * 60 + sm)
	if t < 0:
		t += 1440
	ans += t
print(ans)