
#include<bits/stdc++.h>
using namespace std;
long long n, i=0, s, nto[10000000], lth[10000000], kq=1, m;
bool nt(long long n)
{
    if(n<2)
        return false;
    if(n<4)
        return true;
    if(n%2==0||n%3==0)
        return false;
    for(long long i=5; i*i<=n; i+=6)
        if(n%i==0||n%(i+2)==0)
            return false;
    return true;
}
void sang(long long n)
{
    long long a[n+1];
    long long s=0;
    fill(a+2, a+1+n, 1);
    for(long long i=2; i*i<=n; i++)
        if(a[i]==1)
            for(long long j=i*i; j<=n; j+=i)
                a[j]=0;
    for(long long i=2; i<=n; i++)
        if(a[i]==1)
            {s++; nto[s]=i;}
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin>>n;
    m=sqrt(n);
    sang(m);
    while(n>1 && nt(n)==false)
    {
        s=0;
        i++;
        while(n%nto[i]==0)
            {n/=nto[i]; s++; }
        if(s%2==1) kq*=nto[i];
    }
    if(nt(n)==true)
        kq*=n;
    cout<<kq;
}
