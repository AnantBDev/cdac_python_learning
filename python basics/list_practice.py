# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 07:37:24 2026

@author: PGCP-BDA
"""

lst=[12,13,1,3,4,6]
num=13
#print(num in lst)
#lst.append(34)
#print(lst)

#Appending list
lst.append([10,20,30])

''' Find length '''
#print(len(lst))

# lst.extend([10,20,30])
# print(lst)
# print(len(lst))

# lst.append('test')
# print(lst)
# lst.extend('test')

# print(lst)
# lst.insert(2,100)
# print(lst)

# lst.insert(3,200)
# print(lst)

#To delete from the end
# lst.pop()
# print(lst)
# lst.pop(3)
# print(lst)

# lst.remove(100)
# print(lst.count(100))
# print(lst)

# print(lst.count(10))

# lst1=lst.copy()
# print(lst1)

# lst.reverse()
# print(lst)
# print(lst1)

# lst.sort()
# print(lst)

lst.sort(reverse=True)
print(lst)

a=1,2,'test',3
x=(10,20)
y=(10,)
print(type(y))

def f1(a,b):
    a=a+10
    b=b+20
    return a,b
x,y=f1(10,20)
print(x,y)

print(x,y,sep="$")

#variable no of parameters
def add(a,b,*t):
    s=a+b
    print('tuple',t)
    for num in t:
        s=s+num
    return s

print(add(12,34))
print(add(1,2,3,5,23,24))

a=1,2,3,4
print(a.index(3))

lst=list(a)
print(lst)

a=tuple(lst)
print(a)

lst1=[]
lst=[1,12,3,14,10,7,3,4]
for num in lst:
    if num%2==0 and num>5:
        lst1.append(num)
print(lst,lst1)


#list compression operator
lst2=[num for num in lst if num%2==0 and num>5]
print(lst,lst2)

#filter
lst3=list(filter(lambda num:num%2==0 and num>5,lst))
print(lst,lst3)

lst4=[]
for num in lst:
    lst4.append(num*num)
print(lst4)

lst6=[num*num for num in lst]
print(lst6)

lst5=list(map(lambda num:num*num, lst))
print(lst5)

import functools
s=0
for num in lst:
    s=s+num
print(s)

s=functools.reduce(lambda acc,num:acc+num,lst)
print(s)

s=functools.reduce(lambda acc, num:acc+num, lst, 100)
print(s)

lst=['python', 'perl', 'java']
s=functools.reduce(lambda acc,s:acc+s, lst)
print(s)

import functools
s=fucntools.reduce(lambda acc,s:acc+s[0:3],lst,'')
print(s)


lst=[34, 20, 1, 4, 56, 37]
for num in sorted(lst):
    print(num)
print(lst)

for num in sorted(lst,reverse=True):
    print(num)
print(lst)

for num in reversed(lst):
    print(num)
print(lst)

lst1=[1,2,3,4]
lst2=['Delhi','Pune','Mumbai']
for x,y in zip(lst1,lst2):
    print(x,'----->',y)

for x in zip(lst1,lst2):
    print(x[0],'----->',x[1])

lst=[12,23,11,4,3]    
for i,num in enumerate(lst):
    print(i,'---->',num)

for num in enumerate(lst):
    print(num)
    print(num[0],'---->',num[1])
    
    