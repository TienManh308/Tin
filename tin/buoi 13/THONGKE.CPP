#include <bits/stdc++.h>
using namespace std;
long n, a[1000000], b[15];
int main()
{
    freopen("THONGKE.INP","r",stdin);
    freopen("THONGKE.OUT","w",stdout);
    cin >> n;
    for(long i = 1; i <=n; i++)
    {
        cin >> a[i];
        b[a[i]+1]++;
    }
    for(long i = 1; i<= 11; i++)
    {
        if(b[i] != 0)
            cout << i-1 <<" " << b[i]<< endl;
    }
}
