print ("Ho ten: Phan văn sơn")
print ("MSSV: 235752021610098")

ten = input("Nhập tên người: ")
tach_ten = ten.split()
ho = tach_ten[0]
ten_rieng = " ".join(tach_ten[1:])  
print("Họ:", ho)
print("Tên riêng:", ten_rieng)
