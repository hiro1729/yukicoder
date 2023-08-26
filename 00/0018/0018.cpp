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