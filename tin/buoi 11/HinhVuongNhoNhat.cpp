#include <bits/stdc++.h>
using namespace std;
int a[10];
int main()
{
    for(int i = 1; i <= 4; i++)
        cin >> a[i];
    sort(a+1,a+1+4);
    int m = max(a[4], (a[1] + a[2]));
    cout << m*m;
}
