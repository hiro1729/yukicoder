#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	int mx = 0, mn = 1000;
	while (n--) {
		int m;
		cin >> m;
		mx = max(mx, m);
		mn = min(mn, m);
	}
	cout << mx - mn << '\n';
}