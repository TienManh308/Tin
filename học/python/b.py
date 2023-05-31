a=int(input("Nhap a: "))
b=int(input("Nhap b: "))
k=0
if a>b:
    print("Hic Hic!!!")
else:
    for i in range(a,b+1):
        if i%15==0:
        
            k=k+1
print(k)
