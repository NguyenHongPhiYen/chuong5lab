# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:35:40 2024

@author: Admin
"""

N=int(input("Nhập số nguyên dương N:"))
if N>0:
    print("Số nguyên dương hợp lệ")
else:
   print("Số phải là nguyên dương. Vui lòng nhập lại.")
print(f"Các ước số của {N} là:")
for i in range(1, N + 1):
    if N % i == 0:
        print(i)