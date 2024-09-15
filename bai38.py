# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:51:06 2024

@author: PhiYen
"""
print("Tính S = 1 * 2 * 3 * ... * n (với n lẻ > 0)")
n=int(input("Nhap so nguyen duong n: "))
if n>0 and n%2!=0:
    s=1 
    for i in range(1,n+1,1):
        s*=i
    print(s)
else:
    print("Nhap sai, nhap lai.")
