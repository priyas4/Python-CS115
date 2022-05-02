# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 22:33:38 2022

@author: PRIYAJA
"""

a = int(input("Enter first Number = "))
b = int(input("Enter second Number = "))
c = int(input("Enter third Number = "))
d = int(input("Enter fourth Number = "))
if(a>b and a>c and a>d):
  print("The greatest number = ", a)
elif(b>a and b>c and b>d):
  print("The greatest number = ", b)
elif(c>a and c>b and c>d):
  print("The greatest number = ",c)
else:
  print("The greatest number = ", d)