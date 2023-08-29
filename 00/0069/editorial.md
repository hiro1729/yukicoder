## 考察

頻出問題な気がする。各文字の個数が同じなら並べ替えられることができるが、これはソートして全く同じ文字列になることに言い換えられるので、ソートして比較すればよい。

## コード

``` py
a = input()
b = input()
print("YES" if sorted(a) == sorted(b) else "NO")
```

``` cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	string a, b;
	cin >> a >> b;
	sort(a.begin(), a.end());
	sort(b.begin(), b.end());
	cout << (a == b ? "YES\n" : "NO\n");
}
```