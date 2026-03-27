# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:14:17 2026

@author: PGCP-BDA
"""

from Empservice import *

#add new employee in the list as dictionary

            

choice=0
while choice!=8:
    print(emplst)
    choice=int(input("""
                     1. add new employee
                     2. delete the employee
                     3. update salary
                     4. display in  sorted order of name
                     5. display all
                     6. search by id
                     7. search by name
                     8. exit
                     choice:
                     """))
    match choice:
        case 1:
            status=addnewEmployee()
            if status:
                print("employee added")
            else:
                print("employee not added")
                
        case 2:
            name=input('Enter the name of employee to be deleted')
            status=delEmployee(name)
            if status:
                print(f"Employee with {name} deleted")
            else:
                print("Employee not found")
                
        case 3:
            empid=int(input("enter empid to modify sal"))
            sal=float(input("enter sal"))
            status=updateById(empid,sal)
            if status:
                print("updated successfully")
            else:
                print("not found")
        case 4:
            sortByName()
        case 5:
            displayAll()
            pass
        case 6:
            pass
        case 7:
            name=input("enter name to search")
            lst=searchByName(name)
            if lst!=None:
                displayAll(lst)
            else:
                print("Not found")
        case 8:
            print("Thank you for visiting....")
        case others:
            print("wrong choice")
        
