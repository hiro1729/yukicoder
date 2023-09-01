## 考察

僕は、公式解説とは違って、 $A_1$ を全探索しました。公差を $d$ とすると、 $A_n=A_1+d(N-1)$ なので、これが $L \leq A_n \leq R$ となればいいので、式変形をすると $ \frac{L-i}{N-1} \leq d \leq \frac{R-i}{N-1} $ となります。求める答えは、

$$
\begin{align}
\sum_{i=0}^{M}(\lfloor \frac{R-i}{N-1} \rfloor - \lceil \frac{L-i}{N-1} \rceil + 1)
= \sum_{i=0}^{M}(\lfloor \frac{R-i}{N-1} \rfloor - \lfloor \frac{L-i+N-2}{N-1} \rfloor + 1)
= \sum_{i=0}^{M}(\lfloor \frac{R-i}{N-1} \rfloor - \lfloor \frac{L-1-i}{N-1} \rfloor)
\end{align}
$$

となります。これはfloor_sumそのものです。 $i$ の係数が負になってもいいfloor_sumを使えばOKです。

## コード

``` py
def floor_sum(n, m, a, b):
    ans = 0
    while True:
        if a >= m or a < 0:
            ans += n * (n - 1) * (a // m) // 2
            a %= m
        if b >= m or b < 0:
            ans += n * (b // m)
            b %= m
        y_max = a * n + b
        if y_max < m: break
        n, b, m, a = y_max // m, y_max % m, a, m
    return ans  
for _ in range(int(input())):
	n, m, l, r = map(int, input().split())
	c = 0
	c += floor_sum(m + 1, n - 1, -1, r)
	c -= floor_sum(m + 1, n - 1, -1, l - 1)
	print(c % 998244353)
```

急いで書いたので、C++は後で追加します…