#include <iostream>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	int c[3];
	c[0] = 1; c[1] = 2; c[2] = 3;
	while (m--) {
		int p, q;
		cin >> p >> q;
		p--; q--;
		swap(c[p], c[q]);
	}
	for (int i = 0; i < 3; i++) {
		if (c[i] == n) cout << i + 1 << '\n';
	}
}