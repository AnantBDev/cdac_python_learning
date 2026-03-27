# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 08:32:46 2026

@author: PGCP-B

"""



def displayDiamond(n):
    spcnt=n//2
    for i in range(1,n+1,2):
        print(' '*spcnt,end=' ')
        print('*'*i)
        spcnt=spcnt-1
    spcnt=1
    for i in range(n-2,0,-2):
        print(' '*spcnt,end=' ')
        print('*'*i)
        spcnt=spcnt+1
    
    
n=int(input('Enter the number of lines '))
if n%2==0:
    print('The number should be odd')
else:
    displayDiamond(n)
"""------------------------------------------"""
import sys
lst=[]
def addname(n):
    lst.append(n)
    return True

def displayAll():
    for idx,nm in enumerate(lst,1):
        print(f"{idx} : {nm}")

def deletename(name):
    if name in lst:
        lst.remove(name)
        return True
    else:
        return False

def searchname(oname):
    if oname in lst:
        return lst.index(oname), lst.count(oname)
    else:
        return -1,0
        
    
def updatename(oname,nname):
    pos,cnt=searchname(oname)
    if pos!=-1:
        lst[pos]=nname
        return True
    else:
        return False
    
def displaySortedname(ch):
    if ch==1:
        for nm in sorted(lst):
            print(nm)
    else:
        for nm in sorted(lst, reverse=True):
            print(nm)

    
choice=0
while choice!=7:
    choice=int(input("""
                     1.add new name
                     2.delete name
                     3.update name
                     4.display all
                     5.search name
                     6.display in sorted order
                     7.exit
                     Please enter your choice:
                     """
        ))
    match choice:
        case 1:
            name=input('Enter name')
            status=addname(name)
            if status:
                print('name added')
            else:
                print('name not added')
                
        case 2:
            name=input('Enter name')
            status=deletename(name)
            if status:
                print('name added')
            else:
                print('name not added')
                
        case 3:
            oname=input('Enter name to be updated')
            nname=input('Enter the new name')
            status=updatename(oname, nname)
            if status:
                print('name updated')
            else:
                print('name not updated')
                
        case 4:
            if len(lst)>0:
                displayAll()
            else:
                print('Empty list')
                
        case 5:
            name=input('Enter name')
            pos,cnt=searchname(name)
            if status:
                print(f"{name} found at {pos} count {cnt} ")
            else:
                print('{name} not found')
                
        case 6:
            displayAll()
            
        case 7:
            print(' Exiting .........')
            exit()
            
        case others:
            print('Invalid input')
