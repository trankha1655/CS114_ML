import math
a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2
p = math.sqrt(p*(p-a)*(p-b)*(p-c))
if int(p)-round(p,2) == 0:
    p = int(p)
else:
    p = round(p,2)
if a==b==c:
    print("Tam giac deu, dien tich =",round(p,2))
else:
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
        print("Tam giac vuong, dien tich =",p)
    elif a==b or b==c or a==c:
        print("Tam giac can, dien tich =",p)
    elif a+b>c and a+c>b and b+c>a:
        print("Tam giac thuong, dien tich =",p)
    else: 
        print("Khong phai tam giac")
