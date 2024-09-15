# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:25:42 2024

@author: PhiYen
"""
n=int(input("Nhap so n nguyen duong: "))
tong=0
while n>0:
    tong+=n%10
    n//10
print("Tong cac chu so",tong)
