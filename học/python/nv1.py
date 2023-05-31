n = int(input('nhap so hoc sinh: '))
a = []
for i in range(n):
    ten = input('nhap ten thu' + str(i+1)+':')
    a.append(ten)
print('danh sach lop :')
for i in range(n):
    print(a[i])