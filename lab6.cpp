#include <iostream>
using namespace std;
//4:
double harmonic(int x) {
    if (x == 1)
        return 1.0;
    else
        return 1.0 / x + harmonic(x - 1);
}
//5:
double harmonic() {
    int x;
    cout << "Enter n: ";
    cin >> x;
    if (x == 1)
        return 1.0;
    else
        return 1.0 / x + harmonic(x - 1);
}


int main() {
    double rslt = harmonic();
    double rslt2=harmonic(3);
    cout << rslt2 << endl;
    cout << rslt << endl;
    return 0;
}
