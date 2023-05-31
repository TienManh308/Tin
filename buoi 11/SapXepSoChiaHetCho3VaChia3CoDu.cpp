#include <bits/stdc++.h>
using namespace std;
long n, a[10000], d = 1, k= 1, m = 1;
int main()
{
    cin >> n;
    a[1] = 1;

    while(a[d] < n)
        {a[d+1] = 1 + 3*d;d++;}
    while(a[k+d] <= n)
        {a[k+d] = 2 + 3*(k-1);k++;}
    for(int i = 1; i <= n; i++)
        cout << a[i] << " ";
}
