## 考察

初めに、すべての値段を求めておく。それから、求めたいのは使う硬貨の枚数なので、 $1000$ で割った余りを求める。これから、 $100, 25, 1$ で順に割っていき、使う硬貨の枚数が求められる。

## コード

``` py
l = int(input())
m = int(input())
n = int(input())
y = 100 * l + 25 * m + n
y %= 1000
print(y // 100 + (y % 100) // 25 + y % 25)
```

``` cpp
#include <iostream>
using namespace std;

int main() {
    int l, m, n;
    cin >> l >> m >> n;
    int y = l * 100 + m * 25 + n;
    y %= 1000;
    cout << (y / 100) + (y % 100) / 25 + y % 25 << '\n';
}
```