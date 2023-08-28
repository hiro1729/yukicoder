## 考察

$1$ ゲームごとに考える。文字列 $S$ の長さを $L$ として、 $T$ msでタイプできる文字数を $C = \floor \frac{12C}{1000} \rfloor$ とする。この時、 $L \leqq C$ のときは文字列を全部打てるので、打てる文字数に $L$ を加える。そうでないときは、 $C$ 文字しか打つことができない。なので、打てる文字数に $C$ を加え、打ち逃す文字数に $L-C$ を加える。

## コード

``` py
ok = 0
ng = 0
for _ in range(int(input())):
	t, s = input().split()
	t = int(t)
	l = len(s)
	c = 12 * t // 1000
	if l <= c:
		ok += l
	else:
		ok += c
		ng += l - c
print(ok, ng)
```

``` cpp
#include <iostream>
using namespace std;

int main() {
	int ok = 0, ng = 0;
	int n;
	cin >> n;
	while (n--) {
		int t; string s;
		cin >> t >> s;
		int l = s.size(), c = 12 * t / 1000;
		if (l <= c) ok += l;
		else {
			ok += c;
			ng += l - c;
		}
	}
	cout << ok << ' ' << ng << '\n';
}
```