#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using namespace boost::multiprecision;

int main() {
	cpp_int a, b;
	cin >> a >> b;
	cout << a + b << '\n';
}