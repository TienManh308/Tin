n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()
s = a[-1] * a[-2]
x = a[0] * a[1]
if s >= x:
    print(s)
else:
    print(x)