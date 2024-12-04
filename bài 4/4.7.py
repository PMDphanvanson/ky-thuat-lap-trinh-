print ("Ho ten: Phan văn sơn")
print ("MSSV: 235752021610098")

input_string = input("Nhập chuỗi: ")

output_string = ''.join(char for char in input_string if not char.isdigit())

# In ra chuỗi mới
print("Chuỗi sau khi loại bỏ chữ số:", output_string)
