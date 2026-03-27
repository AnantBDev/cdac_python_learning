# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:40:39 2026

@author: PGCP-BDA
"""

import pymysql

def addnewproduct():
    pid=int(input("Enter pid:"))
    pname=input("Enter pname")
    qty=int(input("Enter qty"))
    price=float(input("Enter price"))
    mfgdate=input("enter date (yyyy-mm-dd)")
    print("Writing Data .....")
    cur.execute("insert into product values(%s,%s,%s,%s,%s)",(pid,pname,qty,price,mfgdate))
    conn.commit()
    print("Data written successfully.....")
    

def displayAll():
    cur.execute("select * from product")
    for row in cur.fetchall():
        print(f"Id:{row[0]} Name:{row[1]} Qty:{row[2]} price:{row[3]} mfgdtae:{ row[4]}")

def deleteById(pid):
    cur.execute("delete from product where pid=%s",(pid,))
    conn.commit()
    return True
def updateById(pid,qty,pr):
    print("updating the data")
    cur.execute("update product set qty=%s,price=%s where pid=%s",(qty,pr,pid))
    print("updated the data")
    conn.commit()
    return True

def displayById(pid):
    cur.execute("select * from product where pid=%s",(pid,))
    row=cur.fetchone()
    if row:
        print(f"Id:{row[0]} Name:{row[1]} qty: {row[2]} price: {row[3]} mfg_date:{row[4]}")
    else:
        print("Record not Found with the given id!")
try:
    conn=pymysql.connect(host='localhost',port=3306,user="root",password="bda123",db="test")
    #print(conn)    
    if conn!=None:
        print("connection done")
    else:
        print("connection failed")
    
except Exception as e:
    print(e)
    
try:
    cur=conn.cursor()
    choice=0
    while choice!=6:
        choice=int(input("""
                         1. Add new Product
                         2. Delete Product
                         3. Modify product info
                         4. Display All
                         5. Display by id
                         6. exit
                         """))
        match choice:
            case 1:
                addnewproduct()
            case 2:
                pid=int(input("Enter Pid: "))
                status=deleteById(pid)
                if status:
                    print("Record deleted")
                else:
                    print("Record not Found!")
            case 3:
                pid=int(input("Enter Pid: "))
                qty=int(input("Enter new qty: "))
                pr=float(input("Enter new price: "))
                status=updateById(pid,qty,pr)
                if status:
                    print("updated successfully")
                else:
                    print("Not found!")
            case 4:
                displayAll()
            case 5:
                pid=int(input("Enter Product id:"))
                displayById(pid)
            case 6:
                print("Exiting ....")
            case others:
                print("Invalid Choice")
                
except Exception as e:
    print("fail")
    print(e)
finally:
    print("Closing database connection ...")
    if conn!= None:
        cur.close()
        conn.close()
    print("Database Connection closed....")