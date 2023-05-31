#include <iostream>
#include <bits/stdc++.h>

using namespace std;
int n;
int main()
{
    cin >> n;
    int a = n / 10;
    int b = n % 10;
    int tong = 45 * a + b * (b + 1)/2;
    cout << tong;
    return 0;
}
