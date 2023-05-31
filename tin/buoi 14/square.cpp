#include <bits/stdc++.h>
using namespace std;
long n;
long long s, a[100000000] ;
int main()
{
    freopen ("square.inp","r",stdin);
    freopen ("square.out","w",stdout);
    cin >> n;
    for (long i = 1; i <= n; i++)
    {
        cin >> a[i];
        long t = sqrt(a[i]);
        if(int(t) * t == a[i])
            s = s + a[i];
    }
    cout << s;
}
