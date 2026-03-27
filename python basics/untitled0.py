# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:26:06 2026

@author: PGCP-BDA
"""

print("Hello world!")
a=23
b=233
if a>b:
    print("maximum is a",a)
    print("end of if")
else:
    print("maximum is b",b)
    print("end of else")
print("outside if")
for i in range(5):
    print(i)
    
age=20
if age>=5 and age<6:
    print("you are in kinder garden")
elif age>=6 and age<14:
    print("You are in Primary School")
else:
    print("You are in secondary school")
    
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
a=num1+num2
print("Addition of ",num1," and ",num2,"=",a)
print("Addition of "+str(num1)+" and"+str(num2)+" = "+str(a))
print(f"The sum of {num1} + {num2} = {a}")

print("Addition of {0} and {1} is {2} ".format(num1,num2,a))

print("hello")
print("Welcome")

print("hello",end=" ")
print("hello")

print(4,5,36,12,sep="|")