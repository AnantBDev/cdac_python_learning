# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 09:42:30 2026

@author: PGCP-BDA
"""

emplst=[]

#adds new emp details as dict into emplst
def addnewEmployee():
    emp={}
    emp_id=int(input("Enter employee id: "))
    ename=input("Enter name: ")
    sal=float(input("Enter salary"))
    dno=int(input("enter dno"))
    dname=input("enter dname")
    lst=[]
    ans='y'
    while ans=='y':
        skill=input("enter skill")
        lst.append(skill)
        ans=input("got more skills to add?(y/n): ")
    
    emp["empid"]=emp_id
    emp["ename"]=ename
    emp["sal"]=sal
    emp["dno"]=dno
    emp["dname"]=dname
    emp["skill"]=skill
    print(emp)
    emplst.append(emp)

def displayall():
    for e in emplst:
        print(f"empid: {e["empid"]},ename: {}")
    
choice=0

while choice!=7:
    choice=int(input(
        """
        1.add new employee
        2.delete the employee
        3.update salary
        4.display in sorted order
        5.display all
        6.search by id
        7.search by name
        8.exit
        """
        ))
    match choice:
        case 1:
            status=addnewemployee()
            if status:
                print("employee added")
            
        case 2:
            
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            displayall()
        case 6:
            pass
        case 7:
            pass
        case 8:
            print("Thank you")
            
        case others:
            print("Invalid choice")