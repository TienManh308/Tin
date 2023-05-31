a = int(input('nhap a: '))
d = int(input('nhap d: '))
n = int(input('nhap n: '))
i = 0
b = [a]
while b[i] < n :
    i+=1
    b.append(a + i * d)
print(b)