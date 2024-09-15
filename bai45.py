# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:05:46 2024

@author: PhiYen
"""
n=int(input("Nhap so nguyen duong n: "))
x=float(input("Nhap so x: "))
if n>0:
    s=0
    s2=0
    for i in range(1,n+1):
        s2=s2+i
        s=s+((x**i)/s2)
    print(s)
else:
    print("Nhap sai, nhap lai.")
