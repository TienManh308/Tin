#include<bits/stdc++.h>
using namespace std;
int bof[60001];
int main()
{
	int a,b,c,d,e;
	cin>>a;
	for(b=1;b<=a;b++)
	{
		cin>>bof[b];
	}
	for(b=2;b<=a;b++)
	{
		cin>>c;
		bof[b]=min(bof[b]+bof[b-1],bof[b-2]+c);
	}
	cout<<bof[a];
}
