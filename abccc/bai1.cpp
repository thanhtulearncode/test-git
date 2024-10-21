#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();
    string ans;
    for (int i = 0; i < n; i++) {
        string s;
        getline(cin, s);
        if (s.substr(0, 2) == "42") {
            int sum = 0;
            for (char c : s) {
                sum += c - '0';
            }
            if (sum == 75) {
                ans = s;
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}
