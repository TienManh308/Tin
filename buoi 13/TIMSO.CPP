#include <bits/stdc++.h>
using namespace std;
long n,a[10000006], s = 1;

void SangNT(long n)
{

    fill(a+1, 1 + a + n, 1);
    a[1] = 0;
    for(long i = 2; i <= sqrt(n); i++)
    {
        if(a[i] == 1)
            for(long j = i*i; j<=n; j+=i)
                a[j] = 0;
    }
}

int main()
{
    freopen("TIMSO.INP","r",stdin);
    freopen("TIMSO.OUT","w",stdout);
    cin >> n;
    SangNT(10000000);
    cout << "2";
    for(long i = 3; i <= 10000000; i+=2)
    {
        if(s == n)
            return 0;
        if(a[i]==1)
            {cout << i;s++;}

    }
}
