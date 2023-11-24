#include <bits/stdc++.h>
using namespace std;

int main() {
	int N, L;
	cin >> N;
	map<int, int> c;
	while (N--) {
		cin >> L;
		c[L]++;
	}
	int max_cnt = 0, ans = -1;
	for (auto [i, j]: c) {
		if (j > max_cnt) {
			max_cnt = j;
			ans = i;
		} else if (j == max_cnt && i > ans) {
			ans = i;
		}
	}
	cout << ans << '\n';
}