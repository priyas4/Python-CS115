# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 18:34:27 2022

@author: PRIYAJA
"""

x=0
sum=0
#in while loop x is initialized to 0, then condition is checked and the value is incremented
while(x<5):
    #since average will be decimal value, I used float
    num=float(input("Enter a number: "))
    sum = sum + num
    x+=1
#total sum is calculated and divided by 5 to find the average of 5 numbers
average = sum / 5
print(average,"is the average")