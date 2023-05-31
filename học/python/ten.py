n = int(input("Nhập số lượng họ tên: "))
names = []

for i in range(n):
    name = input("Nhập họ tên thứ " + str(i+1) + ": ")
    names.append(name)

names.sort(key=lambda x: x.split()[-1])

print("Danh sách họ tên đã được sắp xếp theo tên:")
for name in names:
    print(name)