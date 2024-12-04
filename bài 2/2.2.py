print ("Ho ten: Phan văn sơn")
print ("MSSV: 235752021610098")

import math;
x1=int(input ("Nhap x1: "))
y1=int(input ("Nhap y1: "))
x2=int(input ("Nhap x2: "))
y2=int(input ("nhap y2: "))
d1 = (x2 - x1) * (x2 - x1);
d2 = (y2 - y1) * (y2 - y1);
res = math.sqrt(d1+d2)
print("Khoang cách giua hai diem la:", res);
