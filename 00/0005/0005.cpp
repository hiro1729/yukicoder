#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int l, n;
    cin >> l >> n;
    vector<int> w(n);
    for (int i = 0; i < n; i++) cin >> w[i];
    sort(w.begin(), w.end());
    int ans = 0, s = 0;
    for (int i = 0; i < n; i++) {
        s += w[i];
        if (s > l) break;
        ans++;
    }
    cout << ans << '\n';
}