s = input('nhập ngày: ')
def kiemtra(a):
    b = a.split("-")
    ktnn = 0
    if int(b[2]) % 400 == 0:
        ktnn = 0
    else:
        if int(b[2]) % 4 == 0:
            ktnn = 1
    
    if ktnn == 1:
        if b[1] == '02':
            if 1<= int(b[0]) <=29:
                return True
    else:
        if b[1] == '02':
            if 1<= int(b[0]) <=28:
                return True
    
    if b[1] == '1' or b[1] == '3' or b[1] == '5' or b[1] == '7' or b[1] == '8' or b[1] == '10' or b[1] =='12':
        if 1 <= int(b[0]) <= 31:
            return True
    else:
        if b[1] != '02':
            if 1 <=  int(b[0]) <= 30:
                return True  
    return False

if kiemtra(s) == True:
    print('hop le')
else:
    print('ko hop le')

