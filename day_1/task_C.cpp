#include <iostream>
using namespace std;
 
int main() {
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        
        int total = 3 * n;
        int left = 1;
        int right = total;
        
        for (int j = 0; j < n; j++) {
            cout << left << " " << right - 1 << " " << right << " ";
            left++;
            right -= 2;
        }
        cout << endl;
    }
    
    return 0;
}
