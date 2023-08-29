#include <iostream>
using namespace std;

int main() {
	int x, y, l;
	cin >> x >> y >> l;
	int ans = (abs(x) + l - 1) / l + (abs(y) + l - 1) / l;
	if (y >= 0 && x != 0) ans++;
	else if (y < 0) ans += 2;
	cout << ans << '\n';
}