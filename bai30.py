# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:15:34 2024

@author: Phi Yen
"""

# Nhập tháng và năm từ người dùng
while True:
    try:
        month = int(input("Nhập tháng (1-12): "))
        year = int(input("Nhập năm: "))
        if 1 <= month <= 12:
            break
        else:
            print("Tháng không hợp lệ! Vui lòng nhập lại.")
    except ValueError:
        print("Giá trị nhập vào không hợp lệ! Vui lòng nhập lại.")

# Kiểm tra năm nhuận
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap_year = True
else:
    is_leap_year = False

# Xác định số ngày trong tháng
days_in_month = 0

if month in [1, 3, 5, 7, 8, 10, 12]:  # Các tháng có 31 ngày
    days_in_month = 31
elif month in [4, 6, 9, 11]:  # Các tháng có 30 ngày
    days_in_month = 30
elif month == 2:  # Tháng 2
    if is_leap_year:
        days_in_month = 29
    else:
        days_in_month = 28

# In số ngày trong tháng
print(f"Tháng {month} năm {year} có {days_in_month} ngày.")
