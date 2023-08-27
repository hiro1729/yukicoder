#include <iostream>
using namespace std;

int main() {
    int l, m, n;
    cin >> l >> m >> n;
    int y = l * 100 + m * 25 + n;
    y %= 1000;
    cout << (y / 100) + (y % 100) / 25 + y % 25 << '\n';
}