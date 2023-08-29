## 考察

消費税は $\frac{100+P}{100}%$ である。これを使うと整数の範囲内で計算することができる。答えは $D \times \frac{100+P}{100}$ である。

## コード

``` py
d, p = map(int, input().split())
print(d * (100 + p) // 100)
```

``` cpp
#include <iostream>
using namespace std;

int main() {
	int d, p;
	cin >> d >> p;
	cout << d * (100 + p) / 100 << '\n';
}
```