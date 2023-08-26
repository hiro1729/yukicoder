## 考察

ターンごとに、YESと答えたらA,B,C,Dの中に必ず入っているので、それ以外の可能性を排除する。NOと答えたら、A,B,C,Dの中にはないのでそれらの可能性を排除する。

## コード

``` py
n = int(input())
ok = [True] * 10
for _ in range(n):
	a, b, c, d, s = input().split()
	a, b, c, d = map(int, [a, b, c, d])
	if s == "NO":
		ok[a] = False
		ok[b] = False
		ok[c] = False
		ok[d] = False
	else:
		for i in range(10):
			if i not in [a, b, c, d]:
				ok[i] = False
for i in range(10):
	if ok[i]:
		print(i)
```

``` cpp
#include <iostream>
#include <set>
using namespace std;

int main() {
	int n;
	cin >> n;
	bool ok[10];
	for (int i = 0; i < 10; i++) ok[i] = true;
	for (int i = 0; i < n; i++) {
		int a, b, c, d; string s;
		cin >> a >> b >> c >> d >> s;
		if (s == "NO") {
			ok[a] = false;
			ok[b] = false;
			ok[c] = false;
			ok[d] = false;
		} else {
			for (int i = 0; i < 10; i++) {
				if (i != a && i != b && i != c && i != d) ok[i] = false;
			}
		}
	}
	for (int i = 0; i < 10; i++) {
		if (ok[i]) cout << i << '\n';
	}
}
```