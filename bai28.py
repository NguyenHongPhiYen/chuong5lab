# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:53:13 2024

@author: PhiYen
"""
while True:
    n=input("Nhap vao so n: ")
    n=float(n)
    if n > 0 and n%1==0:
        break
    else:
        print("Nhap sai, nhap lai!")
#In uoc so
print("Các uoc so cua n la: ")
a=int(float(n))
for i in range (1,a+1):
    if a%i==0:
        print(i, end="\t")
    

