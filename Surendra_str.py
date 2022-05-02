# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:21:20 2022

@author: PRIYAJA
"""

import string
str1="Welcome to CS115.\n I'm so excited to have this course in this semester."
#initialize value 1 for total
total=1
#incrementing the count when space or \n is encountered, so that before that word is present and the value
#gets incremented
for i in range(len(str1)):
    if(str1[i] == ' ' or str1 == '\n'):
        total = total + 1
print("1) Number of Words:", total)

#index -1 gets the value of string from end
new=str1[::-1]
print("2) Reverse of the sentence: ", new)

#accessing the index of the word CS115
first=str1[11:16]
#accessing the index of the word course
second=str1[46:54]
print("3) Pick 'CS115' and 'Course' from the sentence and printed out together: ",first,second)

#for each element in the string, when white space is encountered
# it is replaced with ''
for elem in string.whitespace:
    str1 = str1.replace(elem, '')
print("4) Remove all whitespaces and newlines: ",str1)

str1="Welcome to CS115 I'm so excited to have this course in this semester."
x=list(str1)
#got the index position where the word course has to be added
#and it will be joined with the original string
x.insert(17,'course ')
y=''.join(x)
print("5) Add 'course' after 'CS115': ",y)


