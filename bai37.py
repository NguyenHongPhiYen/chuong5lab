# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:44:32 2024

@author: PhiYen
"""
print("Tính S = 2 + 4 + 6 + ... + n (với n chẵn > 0)")
n=int(input("Nhap so nguyen duong n: "))
if n>0 and n%2==0:
    s=0
    for i in range(2,n+2,2):
        s=s+i
    print(s)
else:
    print("Nhap sai, nhap lai.")
        
    
