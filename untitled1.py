# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:07:10 2026

@author: PGCP-BDA
"""

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))

if num1>num2 and num1>num3:
    print(f"{num1} is biggest")
elif num2>num3:
    print(f"{num2} is biggest")
else:
    print(f"{num3} is biggest")
    
    
for i in range(5):
    print(i,end=" ")
print("")
print("Kaccha badam")

n=int(input('Enter num'))
for i in range(2,n):
    print(i,end=',')
print()

for i in range(1,8,2):
    print(i,end=",")




n=int(input("Enter the number"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
    
m=int(input("Enter M:"))
n=int(input("Enter n:"))

for i in range(m):
    print()
    for j in range(n):
        print(j,end=" ")

num=3456
s=0
while num>0:
    d=num%10
    num=num//10
    s=s+d
print("Digit addition: ",s)

