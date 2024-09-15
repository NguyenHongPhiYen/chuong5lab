# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:29:50 2024

@author: PhiYen
"""
print("S(n) = 1 + 1/3 + 1/5 +...+ 1/(2*n+1)")
n=int(input("Nhap so nguyen duong n: "))
if n>=0:
    s=0
    for i in range(0,n+1):
        s=s+(1/(2*i+1))
    print(s)
else:
    print("Nhap sai, nhap lai.")
