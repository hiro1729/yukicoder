## 考察

まずは問題の通りに通りに操作を行う。最終的にNだったindexを出力する。

## コード

``` py
n = int(input())
m = int(input())
c = [1, 2, 3]
for _ in range(m):
	p, q = map(int, input().split())
	p -= 1
	q -= 1
	c[p], c[q] = c[q], c[p]
print(c.index(n) + 1)
```

``` cpp
#include <iostream>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	int c[3];
	c[0] = 1; c[1] = 2; c[2] = 3;
	while (m--) {
		int p, q;
		cin >> p >> q;
		p--; q--;
		swap(c[p], c[q]);
	}
	for (int i = 0; i < 3; i++) {
		if (c[i] == n) cout << i + 1 << '\n';
	}
}
```