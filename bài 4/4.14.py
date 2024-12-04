print ("Họ tên: Phan văn sơn")
print ("MSSV: 235752021610098")

s = input("Nhập chuỗi: ").split()

s.sort()
print("Danh sách sau khi sắp xếp tăng dần:", s)

s.sort(reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:", s)
