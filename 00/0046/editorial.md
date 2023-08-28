## 考察

求めたいのは $\lceil \frac{B}{A} \rceil$ である。これは $\lfloor \frac{A+B-1}{A} \rfloor$ と書けるので、これを計算して出力すればいい。

## コード

``` py
a, b = map(int, input().split())
print((a + b - 1) // a)
```

``` cpp
#include <iostream>
using namespace std;

int main() {
	int a, b;
	cin >> a >> b;
	cout << (a + b - 1) / a << '\n';
}
```