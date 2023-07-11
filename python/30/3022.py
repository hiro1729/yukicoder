ze = int(False)
on = int(True)
th = on + on + on
fi = on + on + th
n = int(input())
for i in range(on, n + on):
	if i % (th * fi) == ze:
		print("FizzBuzz")
	elif i % th == ze:
		print("Fizz")
	elif i % fi == ze:
		print("Buzz")
	else:
		print(i)