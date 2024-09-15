# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:05:35 2024

@author: PhiYen
"""
s=float(input("Quang duong di dc (km): "))
if s<=1:
    print("Tien taxi: 15000đ")
elif s<=5:
    print("Tien taxi: ", 15000 + (s - 1) * 13500,"đ")
elif s>=120:
    print("Tien taxi: ", (15000 + 4*13500 + (s-1)*11000)*0.9)
else:
    print("Tien taxi: ", 15000 + 4*13500 + (s-1)*11000,"đ")
