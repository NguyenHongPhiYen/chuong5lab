# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:38:31 2024

@author: PhiYen
"""
#So nguyen to: la so le chia het cho 1 va chinh no
n=int(input("Nhap so nguyen duong n: "))
dem=0
for i in range (1,n+1):
    if n%i==0:
        dem+=1
if dem==2:
    print(n,"la so nguyen to.")
else:
    print(n,"khong phai la so nguyen to.")
        

