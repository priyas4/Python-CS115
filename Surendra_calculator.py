# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:23:04 2022

@author: PRIYAJA
"""

print("Please enter your choice 1/2/3/4 ")
print("1 Add (+)")
print("2 Subtract (-)")
print("3 Multiply (*)")
print("4 Divide (/)")

while (True):

    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        x = [] #list created
        y = int(input("How many numbers you will input: "))
        # reading the nos
        for i in range(y):
            n = float(input("Enter number: "))
            # the numbers read are appended to the list x
            x.append(n)
        print("Sum of elements in given list is: ", sum(x))
        # if ch is 'no' then come out of while loop
        ch = input("Would you like to repeat another one? (yes/no): ")
        if ch == "no":
            break


    #similar operation is done
    #for subtraction, the value is appended to the list
    elif choice == 2:
        x = []
        y = int(input("How many numbers you will input "))
        for i in range(y):
            n = float(input("Enter number: "))
            x.append(n)

        # subtraction
        s = x[0]
        for i in range(1, len(x)):
            s = s - x[i]
        print("Subtraction of elements in given list is: ", s)
        ch = input("Would you like to repeat another one? (yes/no): ")
        if ch == "no":
            break

    elif choice == 3:
        x = []
        y = int(input("How many numbers you will input "))
        for i in range(y):
            n = float(input("Enter number: "))
            # put in list
            x.append(n)

        # multiplication
        m = x[0]
        # loop through list of numbers x
        for i in range(1, len(x)):
            m = m * x[i]
        print("Multiplication of elements in given list is: ", m)
        ch = input("Would you like to repeat another one? (yes/no): ")
        if ch == "no":
            break

    elif choice == 4:
        x = []
        y = int(input("How many numbers you will input "))
        for i in range(y):
            n = float(input("Enter number: "))
            # put in list
            x.append(n)

        # division
        d = x[0]
        for i in range(1, len(x)):
            d = d / x[i]

        #print result
        print("Division of elements in given list is: ", d)
        ch = input("Would you like to repeat another one? (yes/no): ")
        if ch == "no":
            break
