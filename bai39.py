# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:56:33 2024

@author: PhiYen
"""
print("S(n) = 1 + 1/2 + 1/3 +...+ 1/n")
n=int(input("Nhap so nguyen duong: "))
if n>0:
    s=0
    for i in range (1,n+1,1):
        s=s+(1/i)
    print(s)
else:
    print("Nhap sai, nhap lai.")
