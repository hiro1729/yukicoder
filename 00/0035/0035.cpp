#include <iostream>
using namespace std;

int main() {
	int ok = 0, ng = 0;
	int n;
	cin >> n;
	while (n--) {
		int t; string s;
		cin >> t >> s;
		int l = s.size(), c = 12 * t / 1000;
		if (l <= c) ok += l;
		else {
			ok += c;
			ng += l - c;
		}
	}
	cout << ok << ' ' << ng << '\n';
}