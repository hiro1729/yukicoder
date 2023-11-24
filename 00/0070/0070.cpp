#include <bits/stdc++.h>
using namespace std;

int main() {
	int N;
	cin >> N;
	int ans = 0;
	while (N--) {
		int sh, sm, eh, em;
		char _1, _2;
		cin >> sh >> _1 >> sm >> eh >> _2 >> em;
		int t = eh * 60 + em - (sh * 60 + sm);
		if (t < 0) {
			t += 1440;
		}
		ans += t;
	}
	cout << ans << '\n';
}