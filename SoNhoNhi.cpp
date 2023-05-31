#include <bits/stdc++.h>
using namespace std;
int a1, a2, a3 ,a4, a5;

int main()
{
    cin >> a1 >> a2 >> a3 >> a4 >> a5;
    int m1 = max(a1, a2);
    int m2 = min(a1, a2);
    if(m1 > a3)
        m1 = a3;
    if(m2 < a4)
        m2 = a4;
    if(m1 > a4)
        m1 = a4;
    if(m2 < a5)
        m2 = a5;
    if(m1 > a5)
        m1 = a5;
    cout << m1;
}
