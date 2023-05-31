a = [int(j) for j in input('nhap day a: ').split()]
b = [int(j) for j in input('nhap day b: ').split()]

l = len(a)
c = []
for i in range(l):
    if a[i] in b:
        c.append(a[i])
c.sort()

i = 1
while i < len(c):
    if c[i] == c[i-1]:
        del c[i]
    else:
        i += 1
print(c)