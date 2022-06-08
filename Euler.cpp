#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void euler(int n, vector<int> &v) {
    if (n == 1) {
        v.push_back(1);
        return;
    }
    euler(n - 1, v);
    v.push_back(n);
}

int main() {
    int n;
    cin >> n;
    vector<int> v;
    euler(n, v);
    sort(v.begin(), v.end());
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;
    return 0;
}