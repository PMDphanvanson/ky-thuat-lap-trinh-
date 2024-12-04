print ("Họ tên: Phan văn sơn")
print ("MSSV: 235752021610098")

s = input("Nhập các từ tiếng Anh cách nhau bởi dấu cách: ")

words = s.split()

words.sort()

print("Các từ theo thứ tự từ điển:")
for word in words:
    print(word)
