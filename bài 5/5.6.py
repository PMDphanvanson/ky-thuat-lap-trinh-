print("phan văn sơn")
print("235752021610098")
# Module tìm phần tử lớn nhất và nhỏ nhất
def find_largest_and_smallest(arr):
    arr.sort()  # Sắp xếp danh sách
    smallest = arr[0]  # Phần tử nhỏ nhất là phần tử đầu tiên
    largest = arr[-1]  # Phần tử lớn nhất là phần tử cuối cùng
    return smallest, largest

# Chương trình chính
def main():
    # Nhập số lượng phần tử
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    
    # Nhập các giá trị của phần tử vào danh sách
    arr = []
    prin
