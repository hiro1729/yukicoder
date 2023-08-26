#include <iostream>
#include <set>
using namespace std;

int main() {
	int n;
	cin >> n;
	bool ok[10];
	for (int i = 0; i < 10; i++) ok[i] = true;
	for (int i = 0; i < n; i++) {
		int a, b, c, d; string s;
		cin >> a >> b >> c >> d >> s;
		if (s == "NO") {
			ok[a] = false;
			ok[b] = false;
			ok[c] = false;
			ok[d] = false;
		} else {
			for (int i = 0; i < 10; i++) {
				if (i != a && i != b && i != c && i != d) ok[i] = false;
			}
		}
	}
	for (int i = 0; i < 10; i++) {
		if (ok[i]) cout << i << '\n';
	}
}