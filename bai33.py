# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:20:04 2024

@author: PhiYen
"""
import math
while True:
    n=int(input("Nhap n: "))
    if n>0:
        sqrt_n=math.isqrt(n)
        if sqrt_n*sqrt_n==n:
            print(n,"la so chinh phuong.")
            break
        else:
            print(n,"khong phai la so chinh phuong.")
            break
    else:
        print("Nhap sai, nhap lai.")