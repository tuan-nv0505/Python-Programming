#
#
# '''
# 2. Viết chương trình tìm số lớn nhất của 2 số nguyên a và b.
# '''
#
# a = int(input())
# b = int(input())
#
# if a - b > 0:
#     print(a)
# elif a - b < 0:
#     print(b)
# else:
#     print(a, b)
#
#
# '''
# 3. Viết chương trình nhận vào số nguyên n. Xuất ra màn hình kết quả trị tuyệt đối
# của số nguyên đó.
# '''
#
# n = int(input())
#
# if n >= 0:
#     print(n)
# else:
#     print(-n)
#
# '''
# 4. Viết chương trình nhận vào 2 số nguyên. Xuất ra màn hình kết quả so sánh giữa hai số (số thứ nhất lớn hơn, nhỏ hơn hay hai số bằng nhau).
# '''
#
# a = int(input())
# b = int(input())
#
# if a - b > 0:
#     print(f'{a} > {b}')
# elif a - b < 0:
#     print(f'{a} < {b}')
# else:
#     print(f'{a} = {b}')
#
#
# '''
#     5. Viết chương trình nhận vào điểm tích lũy của 1 sinh viên. Xuất ra màn hình kết quả xếp loại của sinh viên đó dựa trên điểm tích lũy. Biết rằng:
#     - Điểm tích lũy từ 9 trở lên xếp loại xuất sắc.
#     - Điểm tích lũy từ 8 đến dưới 9 xếp loại giỏi.
#     - Điểm tích lũy từ 7 đến dưới 8 xếp loại khá.
#     - Điểm tích lũy từ 6 đến dưới 7 xếp loại trung bình khá.
#     - Điểm tích lũy từ 5 đến dưới 6 xếp loại trung bình.
#     - Điểm tích lũy dưới 5 là yếu.
# '''
#
# x = float(input())
#
# if x >= 9:
#     print(f'diem hien tai: {x}')
#     print(f'diem lam tron: {round(x)}')
#     print('xuat sac')
# elif x >= 8:
#     print(f'diem hien tai: {x}')
#     print(f'diem lam tron: {round(x)}')
#     print('gioi')
# elif x >= 7:
#     print(f'diem hien tai: {x}')
#     print(f'diem lam tron: {round(x)}')
#     print('kha')
# elif x >= 6:
#     print(f'diem hien tai: {x}')
#     print(f'diem lam tron: {round(x)}')
#     print('trung binh kha')
# elif x >=5 :
#     print(f'diem hien tai: {x}')
#     print(f'diem lam tron: {round(x)}')
#     print('trung binh')
# else:
#     print(f'diem hien tai: {x}')
#     print(f'diem lam tron: {round(x)}')
#     print('yeu')

'''
# 6. Viết chương trình nhận vào năm. Xuất ra màn hình thông báo năm đó là năm nhuần hay năm không nhuần? Biết rằng năm nhuần là năm có 366 ngày. Năm
# nhuần còn là năm chia hết cho 400 hoặc chia hết cho 4 nhưng không chia hết cho 100.
# '''
#
# y = int(input())
#
# if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#     print(f'{y} la nam nhuan')
# else:
#     print(f'{y} la nam khong nhuan')

'''
# 7. Viết chương trình nhận vào tháng. Xuất ra màn hình số ngày của tháng đó. Giao diện chương trình khi thực hiện được mô phỏng ở 2 ví dụ dưới đây:
# Ví dụ 1:
# Nhap thang: 2
# So ngay cua thang 2 la 28 hoac 29 ngay Ví dụ 2:
# Nhap thang: 3
# So ngay cua thang 3 la 31 ngay
# '''
#
# m = int(input('Nhap thang: '))
# y = int(input('Nhap nam: '))
#
# if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
#     print(f'So ngay cua thang {m} la: {31}')
# elif m == 4 or m == 6 or m == 9 or m == 1:
#     print(f'So ngay cua thang {m} la: {30}')
# else:
#     if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#         print(f'So ngay cua thang {m} la: {29}')
#     else:
#         print(f'So ngay cua thang {m} la: {28}')

# '''
# 9. Viết chương trình có chức năng như máy tính cầm tay (sử dụng if-else) - Nhận vào 2 số nguyên và 1 phép toán ( + - * / )
# - Xuất ra màn hình kết quả tương ứng.
# Lưu ý: phép chia cho 0 thì phải thông báo là lỗi chia 0. Phép chia thực hiện lấy kết quả có 2 chữ số thập phân.
# Giao diện chương trình khi thực hiện được mô phỏng ở 3 ví dụ dưới đây.
# Ví dụ 1:
# Nhap 2 so nguyen va 1 phep toan: 1 3 / 1 / 3 = 0.33
# Ví dụ 2:
# Nhap 2 so nguyen va 1 phep toan: 2 0 / Loi chia 0
# Ví dụ 3:
# Nhap 2 so nguyen va 1 phep toan: 3 5 + 3+5=8
# '''
#
# a = int(input("Nhap so a: "))
# b = int(input("Nhap so b: "))
# operator = input("Nhap toan tu ( + - * / ): ")
#
# if operator == '+':
#     print(f'{a} + {b} = {a + b}')
# elif operator == '-':
#     print(f'{a} - {b} = {a - b}')
# elif operator == '*':
#     print(f'{a} * {b} = {a * b}')
# else:
#     if b == 0:
#         print('loi chia 0')
#     else:
#         print(f'{a} / {b} = {a / b}')
#
# '''
# 10. Viết chương trình nhận vào 1 số nguyên. Xuất ra màn hình số nguyên đó là số
# chẵn hay số lẻ.
# '''
#
# x = int(input())
#
# if x % 2 == 0:
#     print('so chan')
# else:
#     print('so le')

# '''
# 11. Viết chương trình nhận vào 1 số nguyên. Xuất ra màn hình số nguyên đó là số âm? Số dương hay số 0 ?
# '''
#
# x = int(input())
#
# if x > 0:
#     print('so duong')
# elif x < 0:
#     print('so am')
# else:
#     print('so 0')

# '''
# 12. Viết chương trình giải và biện luận phương trình bậc nhất: ax + b = 0.
# '''
#
# a, b = int(input()), int(input())
#
# if a == 0 and b != 0:
#     print('phuong trinh vo nghiem')
# elif a == 0 and b == 0:
#     print('phuong trinh vo so nghiem')
# else:
#     print(f'phuong trinh co nghiem la: {-b/a}')


'''
15. Viết chương trình nhận vào số đo 3 cạnh của 1 tam giác.
Kiểm tra xem 3 cạnh đó có hợp lệ hay không? Nếu hợp lệ thì tam giác đó là loại tam giác gì
(đều, vuông, cân, vuông cân hay thường) ?
'''

# a = int(input("Nhap cannh a: "))
# b = int(input("Nhap cannh b: "))
# c = int(input("Nhap cannh c: "))
#
# is_equilateral = False
# is_balance = False
# is_square = False
#
# if (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and c + b > a):
#     if a == b and b == c and a == c:
#         is_equilateral = True
#
#     if a == c or a == b or b == c:
#         is_balance = True
#
#     if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#         is_square = True
#
#     if is_equilateral:
#         print('tam giac deu')
#
#     if is_square:
#         print('tam giac vuong')
#
#     if is_balance:
#         print('tam giac can')
#
#     if is_square and is_balance:
#         print('tam giac vuong can')
#
#     if not is_balance and not is_equilateral and not is_square:
#         print('tam giac thuong')
# else:
#     print('tam giac khong hop le')

'''
13. Viết chương trình giải và biện luận phương trình bậc hai: ax2 + bx + c = 0.
'''

import math

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

if a == 0:
    if b == 0 and c != 0:
        print("Phuong trinh vo nghiem")
    elif b == 0 and c == 0:
        print("Phuong trinh vo so nghiem")
    else:
        print(f"Phuong trinh co nghiem duy nhat la: {-c/b}")
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        print(f"Phuong trinh co nghiem kep: {-b/(2*a)}")
    else:
        print(f"Phuong trinh co 2 nghiem phan biet: x1 = {(-b - math.sqrt(delta)) / (2*a):.3f}, x2 = {(-b + math.sqrt(delta)) / (2*a):.3f}")



