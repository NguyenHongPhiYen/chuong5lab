# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:09:30 2024

@author: PhiYen
"""

a=int(input("Nhap so nguyen duong a: "))
b=int(input("Nhap so nguyen duong b: "))
c=int(input("Nhap so nguyen duong c: "))
while not a+b>c and a+c>b and b+c>a:
    print("Ba canh do khong tao thanh tam giac.")
    break
else:
    print("Ba canh tao thanh tam giac.")
while True:
    if a==b or a==c or b==c:
       print("Tam giac can.")
       break
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
       print("Tam giac vuong.")
       break
    if a==b==c:
       print("Tam giac deu.")
       break
    else:
       print("Tam giac thuong.")
       break