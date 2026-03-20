# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:50:19 2026

@author: PGCP-BDA
"""


setA={1,2,3,4,5}
setB={4,5,11,12}
print(setA, setB)

#displays all values of set A and setB and common values
print(setA.union(setB),setA|setB)  
#give only common values
print(setA.intersection(setB),setA&setB) 


print(setA.difference(setB),setA-setB)
print(setA.symmetric_difference(setB),setA^setB) 

setA=setA-setB
print(setA)

setA.symmetric_difference_update(setB)
print(setA)
setA=setA^setB
print(setA)