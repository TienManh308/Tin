import math
print ('nhập 3 cạnh')
a = int(input())
b = int(input())
c = int(input())
cv = a+b+c
print('chu vi la: ',cv)
p = (a+b+c)/2
s1 = p*(p-a)*(p-b)*(p-c)
s = math.sqrt(s1)
print('diện tích là: ', s)
