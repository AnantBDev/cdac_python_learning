# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:54:33 2026

@author: PGCP-BDA
"""

'''

Dictionary is used to store
key:value pairs
example:
    {'pune':'3000Kms',
     'Mumbai':'2000Kms'}
Dictionary:
1.It is mutable
2.It stores key value pairs,keys are unique.
Any immutable object can be the key.
3.It is ordered collection
4.The value can be retrived very fast,
if you know the key.But if you  want to find
the key based on value,then you need to navigate
the dictoionary.
5.Dictionary is represented by using {}
6.to create a empty dictionary you can use,
d={},to create empty set s=set()

TO add a key
c={}
c['BDA']=240
c['BDA']=300    
'''

d={'BDA':60,'DAC':240,'DVLSI':80}
#add new key value pair

d['dhpsa']=75
#updates the value of present dbda to new value
d['DBDA']=100

print(d)
#to display value, if key exists
'''
If the value is present it will display or
throws an exception
'''
print(d['DAC'])

'''
If we are not sure if the key is not 
present in the dictionary we can use
get()

'''
p=d.get('BDA','key not present')
print(p)
v=d.get('AI','Key not in dict')
print(v)

'''
set default function can be used to add
new key and default value to the dictionary
if the key is not present in the dictionary
'''

v=d.setdefault('BDA11',-10)
print(v)

'''

The popitem() function will delete the last
entry of the dictionary.
'''

k,v=d.popitem()
print(k,v)
print(d)
'''
To delete a particular value
'''
v=d.pop('Dhpcsa',-1) #if the key is found then it will be deleted from the dict and stored in v

#navigating through the dict to find a value
#The below loop will search for the keys
for k in d.keys():#['DAC','DBDA']
    if d[k]>80:
        print(k)
'''
The Second way of navigating through the dict
is by using items() function in a for loop
'''

for k,v in d.items():
    if v>80:
        print(k)
print(d)        

d={'a':100,'b':20}
d1={'b':230,'c':56,'x':100}

'''
To add all keys in d from d1
'''
d.update(d1)
print(d)
#**d implies that a whole dictionary is getting passed
#if you pass two different dictionaries in the below fashion
#then the two dictionaries will get combined.
d3={**d,**d1}
print(d3)
