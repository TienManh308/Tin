#include <bits/stdc++.h>
using namespace std;
long long n, s;
int main()
{
    freopen("cube.inp","r",stdin);
    freopen("cube.out","w",stdout);
    cin >> n;
    if(n <= 10000)
    {
        s = (n + 1) * n * (n + 1) * n / 4;
        s = s % 1000000007;
        cout << s;
        return 0;
    }
    else
    {
        s = 10001 * 10000 * 10001 * 10000 / 4
        s = s % 1000000007;
        for(int i = 10001; i <= n; i++)
            s = (s + i*i*i) % 1000000007;
        cout << s;
    }
    return 0;
}
