#include <bits/stdc++.h>
using namespace std;
long n, a[10000], d = 1, k = 1, m ;
int main()
{
    cin >> n;
    a[1] = 1;

    while(a[d] < n)
        {a[d+1] = 1 + 3*d;d++;}
        a[d+1]=2;
    while(a[k+d+1] <= n)
        {a[k+d+2] = 2 + 3*k;k++;}
    for(int i = 1; i <= n; i++)
        cout << a[i] << " ";
}
