#include <bits/stdc++.h>
using namespace std;
long n, s, a[10005];
int main()
{
    freopen("GAME.INP","r",stdin);
    freopen("GAME.OUT","w",stdout);
    cin >> n;
    for(int i = 1; i <= n; i++)
        cin >> a[i];
    sort(a +1, a + 1 + n, greater <int>());
    cout << a[1] + a[2] + a[3];
}
