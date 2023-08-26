## 考察

グループは3つ以上になるので、最大の数字、最小の数字、その他、と分けることができる。だから、平均の差の最大値は、(最大の数字)-(最小の数字)になる。

## コード

``` py
n = int(input())
k = int(input())
m = [int(input()) for _ in range(n)]
print(max(m) - min(m))
```

``` cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	int mx = 0, mn = 1000;
	while (n--) {
		int m;
		cin >> m;
		mx = max(mx, m);
		mn = min(mn, m);
	}
	cout << mx - mn << '\n';
}
```