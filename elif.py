# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:11:05 2022

@author: PRIYAJA
"""
#elif statement

#declare a variable
name = input("Enter a Name:")

if name == "Max":
    print("Name entered is:",name)
elif name == "Leo":
    print("Name entered is:",name)
elif name == "Roy":
    print("Name entered is:",name)
elif name == "Eli":
    print("Name entered is:",name)
else:
    print("The name entered is invalid")
#if the name matches the given name output will be "Name entered is ...."
#else invalid name
#we cannot start statment with elif we have to start with if


#if there are two different "if condition" it will print two times
name = input("Enter a Name:")

if name == "Max":
    print("Name entered is:",name)
if name == "Max":
    print("Name entered is:",name)
elif name == "Leo":
    print("Name entered is:",name)
elif name == "Roy":
    print("Name entered is:",name)
elif name == "Eli":
    print("Name entered is:",name)
else:
    print("The name entered is invalid")
    
    

#nested ifelse statement
#finding a number postive or negative while checking whether they are odd or even
x = 10
if x < 0:
    print("x is negative")
else:
    print("x is positive")
    if (x%2)==0:
        print("x is even")
    else:
        print("x is odd")
        
        

