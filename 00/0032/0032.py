l = int(input())
m = int(input())
n = int(input())
y = 100 * l + 25 * m + n
y %= 1000
print(y // 100 + (y % 100) // 25 + y % 25)