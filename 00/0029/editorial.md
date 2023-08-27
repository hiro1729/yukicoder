## 考察

アイテムは全部もらうことにする。同じアイテムがあるとき、それを「任意のアイテム4つ」に使用するのは無駄である。なので、cntというlist(または配列)にそれぞれのアイテムの個数を保存し、「同じアイテム2つ」に最大限使用する。残ったアイテムは「任意のアイテム4つ」に使えばいい。

## コード

``` py
n = int(input())
cnt = [0] * 10
for i in range(n):
	a, b, c = map(int, input().split())
	cnt[a - 1] += 1
	cnt[b - 1] += 1
	cnt[c - 1] += 1
s = 0
t = 0
for i in cnt:
	s += i // 2
	t += i % 2
print(s + t // 4)
```

``` cpp
#include <iostream>
using namespace std;

int main() {
	int n, a, b, c;
	cin >> n;
	int cnt[10];
	for (int i = 0; i < 10; i++) cnt[i] = 0;
	while (n--) {
		cin >> a >> b >> c;
		cnt[--a]++;
		cnt[--b]++;
		cnt[--c]++;
	}
	int s = 0, t = 0;
	for (int i: cnt) {
		s += i / 2;
		t += i % 2;
	}
	cout << s + t / 4 << '\n';
}
```