a = [int(i) for i in input('nhap:').split()]
b=[]
l = len(a)
i = 0
while i < l:
    if a[i] % 2 == 0:
        b.append(a[i])
    i += 1
print(b)