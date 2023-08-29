## 考察

$C$ 回食べるとすると、 $C$ は $C \times (2 \times K) < L$ を満たす最大の $C$ である。
よって、求める答えは $\lfloor {L - 1}{2 \times K} \rfloor \times K$ である。

## コード

``` py
l, k = map(int, input().split())
print((l - 1) // (2 * k) * k)
```

``` cpp
#include <iostream>
using namespace std;

int main() {
	int l, k;
	cin >> l >> k;
	cout << (l - 1) / (2 * k) * k << '\n';
}
```