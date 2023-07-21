s = input()
t = [[20104, 20063, 19892, 20011, 19874, 20199, 19898, 20163, 19956, 19841][i] - s.count(str(i)) for i in range(10)]
print(t.index(-1), t.index(1))