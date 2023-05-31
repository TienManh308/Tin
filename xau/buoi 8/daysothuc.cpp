#include <bits/stdc++.h>
using namespace  std;
float a[1000], s, sa, sd, sc, sl; int n;
int main()
{
    cin >> n;
    for (int i = 0; i <= n; i++)
    {
        cin >> a[i];
        s+=a[i];
        if(s > 0)
            sd += a[i];
        else
            sa += a[i];
        if (a[i] % 2 ==0)
            sc += a[i];
        else
            sl += a[i]
    }
    cout << "tong day: " << s << endl;
    cout << "tong so am: " << sa << endl;
    cout << "tong so duong: " << sd << endl;
    cout << "tong so chan: " << sc << endl;
    cout << "tong so le: " << sl;
}
