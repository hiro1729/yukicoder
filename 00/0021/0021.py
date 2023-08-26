n = int(input())
k = int(input())
m = [int(input()) for _ in range(n)]
print(max(m) - min(m))