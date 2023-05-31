#include <bits/stdc++.h>
using namespace std;
long n, a[1000000];
int main()
{
    cin >> n;
    int dem = 1;
    for(int i = 1; i <= n; i ++)
        cin >> a[i];
    sort(a+1, a+1+n, greater<long>());
    for(int i = 2; i <= n; i ++)
    {
        if(a[1] == a[i])
            dem ++;
        else
            break;
    }
    cout << dem << endl << a[1];

}
