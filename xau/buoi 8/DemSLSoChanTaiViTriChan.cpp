#include <bits/stdc++.h>
using namespace std;
int n, a[1000],d;
int main()
{
    cin>>n;
    for(int i=1; i <= n; i++)
    {
        cin>>a[i];
        if(a[i] % 2 == 1 && i % 2==0)
            d++;
    }
    cout<<d;
}
