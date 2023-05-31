s = []

s= input('nhap :')
m=0
for i in range(len(s)):
    if '0' <= s[i] <= "9":
        m+=1
        break
if m == 0:
    print('ko co')
else:
    print('co')