# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 09:30:10 2022

@author: PRIYAJA
"""

n = int(input("Enter a Number"))
if n%2==0 and n%3==0:
    print(n,"is even")
    print(n,"is divisible by 3")
elif n%2==0 and n%3!=0:
    print(n,"is even")
    print(n,"is not divisible by 3")
elif n%2!=0 and n%3==0:
    print(n,"is odd")
    print(n,"is divisible by 3")
else:
    print(n,"is odd")
    print(n,"is not divisible by 3")