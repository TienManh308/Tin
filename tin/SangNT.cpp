#include <bits/stdc++.h>
using namespace std;
long a[10000000], n;
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
    cin >> n;
    SangNT(n);
    for(long i = 2; i<= n; i++)
        if(a[i] == 1)
            cout << i << " " ;
}
