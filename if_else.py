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


'''
    5. Viết chương trình nhận vào điểm tích lũy của 1 sinh viên. Xuất ra màn hình kết quả xếp loại của sinh viên đó dựa trên điểm tích lũy. Biết rằng:
    - Điểm tích lũy từ 9 trở lên xếp loại xuất sắc.
    - Điểm tích lũy từ 8 đến dưới 9 xếp loại giỏi.
    - Điểm tích lũy từ 7 đến dưới 8 xếp loại khá.
    - Điểm tích lũy từ 6 đến dưới 7 xếp loại trung bình khá.
    - Điểm tích lũy từ 5 đến dưới 6 xếp loại trung bình.
    - Điểm tích lũy dưới 5 là yếu.
'''

x = float(input())

if x >= 9:
    print(f'diem hien tai: {x}')
    print(f'diem lam tron: {round(x)}')
    print('xuat sac')
elif x >= 8:
    print(f'diem hien tai: {x}')
    print(f'diem lam tron: {round(x)}')
    print('gioi')
elif x >= 7:
    print(f'diem hien tai: {x}')
    print(f'diem lam tron: {round(x)}')
    print('kha')
elif x >= 6:
    print(f'diem hien tai: {x}')
    print(f'diem lam tron: {round(x)}')
    print('trung binh kha')
elif x >=5 :
    print(f'diem hien tai: {x}')
    print(f'diem lam tron: {round(x)}')
    print('trung binh')
else:
    print(f'diem hien tai: {x}')
    print(f'diem lam tron: {round(x)}')
    print('yeu')