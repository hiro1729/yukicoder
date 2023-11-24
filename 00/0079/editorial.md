## 考察

各レベルでカウント数を持っておく。Counterやmapで持っておくと計算しやすい。回答が最も多いものとレベルを更新していく。

## コード

``` py
from collections import Counter
N = int(input())
L = list(map(int, input().split()))
c = Counter(L)
max_cnt = 0
ans = -1
for i, j in list(c.items()):
	if j > max_cnt:
		max_cnt = j
		ans = i
	elif j == max_cnt and i > ans:
		ans = i
print(ans)
```

``` cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	int N, L;
	cin >> N;
	map<int, int> c;
	while (N--) {
		cin >> L;
		c[L]++;
	}
	int max_cnt = 0, ans = -1;
	for (auto [i, j]: c) {
		if (j > max_cnt) {
			max_cnt = j;
			ans = i;
		} else if (j == max_cnt && i > ans) {
			ans = i;
		}
	}
	cout << ans << '\n';
}
```