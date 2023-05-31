#include <bits/stdc++.h>
using namespace std;
long n, a[100000000], dem;
int TongUoc(long x)
{
    long s = 1 ;
    for( long i = 2; i <sqrt(x); i ++)
        if(x % i == 0)
            s = s + i + x/i;
    long k = sqrt(x);
    if(x == int(k) * k)
        s += k;
    return s;
}
int main()
{
    freopen ("tiny.inp","r",stdin);
    freopen ("tiny.out","w",stdout);
    cin >> n;
    for (long i = 1; i <= n; i++)
    {
        cin >> a[i];
        if(a[i] < TongUoc(a[i]))
            dem ++;
    }
    cout << dem;
}
