# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:38:33 2024

@author: PhiYens
"""
print("Tính S = 1*2 + 2*2 + 3*2 + ... + n*2")
n=int(input("Nhap so nguyen duong n: "))
if n>0:
    s=0
    for i in range(1,n+1):
        s=s+(i**2)
    print(s)
else:
    print("Nhap sai, nhap lai.")
    
