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