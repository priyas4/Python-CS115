# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:07:50 2022

@author: PRIYAJA
"""
#creating a list
list1 = list()
#make sure three elements are read from the list

for i in range(1):
    x = input("Enter the first element: ")
    #appending the element read to the list
    list1.append(x)
    
for i in range(1):
    x = input("Enter the second element: ")
    #appending the element read to the list
    list1.append(x)
    
for i in range(1):
    x = input("Enter the third element: ")
    #appending the element read to the list
    list1.append(x)

print('The list is',list1)
# using pop to pop the first element of the list
list1.pop(0)
print('After removing first element', list1)

#initialize sum to 0
sum=0
# for the element present in the list, sum is found
for l in list1:
    sum = sum + int(l)
    
print('Adding the remaining numbers the sum is: ',sum)