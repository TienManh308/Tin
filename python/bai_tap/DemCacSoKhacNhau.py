a = [int(j) for j in input('nhap:').split()]
a.sort()
l = len(a)
d = 1
for i in range(l - 1):
    if a[i] != a[i + 1]:
        d += 1
print(d)