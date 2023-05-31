a=int(input("Nhap A:"))
b=int(input("Nhap B: "))
k=0
if a>b:
    print("Nhap lai ban oi!!!")
else:
    while a< b:
        a=(107/100)*a
        k+=1
    print(k)

