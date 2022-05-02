# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:56:21 2022

@author: PRIYAJA

"""

#1
#if else statement
#declare variable
x = 100

if x == 100:
    print("x is = ",x)
#x value will be declared


#2
#if the condition is not fulfilled
x = 100

if x != 100:
    print("x is = ",x)
#nothing will be displayed


#3
#x value is changed
x = 99

if x != 100:
    print("x is = ",x)
#x value will be 99


#4
#we can also write  print statment next line to print value of x
x = 99

if x != 100:
    print("x is = ")
    print(x)
#x will be printed in next line


#5
#if we add print(finish)
x = 99

if x != 100:
    print("x is = ")
    print(x)
print("finish")
#finish will be printed after printing 99


#6
#if x vlaue is changed back to 100
#then we add print(finish)
x = 100

if x != 100:
    print("x is = ")
    print(x)
print("finish")
#finish will be printed


#7
#to check whether the value of x is positive or negative

x = 100

if x != 100:
    print("x is = ")
    print(x)
if x>0:
    print("x is positive")
else:
    print("x is negative")
    
    
print("finish")
#if x is above zero it will print positve else negative
# if x = 100 it will print "x is positive"
#if x = -100 it will print "x is negative"



#8
#if we try to use logical operators
x = -100

if x != 100 or x>0:
    print("x is = ")
    print(x)
if x>0:
    print("x is positive")
else:
    print("x is negative")
    
    
print("finish")
#output will be the same, as it has to satisfy one condition



#9
#use and operator
x = -100

if x != 100 and x>0:
    print("x is = ")
    print(x)
if x>0:
    print("x is positive")
else:
    print("x is negative")
    
    
print("finish")
# output will just show "x is negative" with "finish