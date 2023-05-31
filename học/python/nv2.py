s= input('nhap :')
kq = False
for i in range(len(s)-1):
    if s[i] == '1' and s[i+1] == '0':
        kq = True
        break
if kq == True:
    print('chua so 10')
else:
    print('chua so 10')