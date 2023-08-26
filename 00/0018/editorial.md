## 考察

1文字ずつ復号していく。

## コード

``` py
def b(i, c):
	return chr(ord('A') + (ord(c) - ord('A') - i) % 26)
s = input()
print(''.join(b(i + 1, c) for i, c in enumerate(s)))
```

C++のコードでは、26で割った余りが負にならないために1300を足している。(文字列の長さの上限、つまりiの上限が1024だからそれより大きい26の倍数ならOK。)

``` cpp
#include <iostream>
using namespace std;

char b(int i, char c) {
	return 'A' + (c - 'A' - i + 1300) % 26;
}

int main() {
	string s;
	cin >> s;
	for (int i = 0; i < s.size(); i++) cout << b(i + 1, s[i]);
	cout << '\n';
}
```