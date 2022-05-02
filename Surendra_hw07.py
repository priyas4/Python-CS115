# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:04:19 2022

@author: PRIYAJA
"""

#reading the count of numbers from the user
number = int(input("Enter the count of numbers: "))
#initializing the value of sum to 0
sum = 0
#iterating over the given count using for loop
for i in range(number):
    #adding the integer to the sum
    sum += int(input("Enter an integer: "))
#calculating the average
average=sum / number
#printing the output
print("The average is: ", average)
