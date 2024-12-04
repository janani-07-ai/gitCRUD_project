from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="ROOT",database="school")

def insert(NAME,AGE,GRADE):
    res=con.cursor()
    sql= "INSERT INTO USERS(NAME,AGE,GRADE) values (%s,%s,%s)"
    user=(NAME,AGE,GRADE)
    res.execute(sql,user)
    con.commit()
    print("Data inserted successfully...")

def update(NAME,AGE,GRADE,ID):
    res= con.cursor()
    sql= "update users set NAME=%s,AGE=%s,GRADE=%s where ID=%s"
    user=(NAME,AGE,GRADE,ID)
    res.execute(sql,user)
    con.commit()
    print("Data updated successfully.....")

def select():
    res=con.cursor()
    sql="SELECT ID,NAME,AGE,GRADE from users"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","GRADE"]))

def delete(ID):
    res=con.cursor()
    sql="delete from users where ID=%s"
    user=(ID,)
    res.execute(sql,user)
    con.commit()
    print("Data deleted successfully........")

while True:
    print("1.Insert data")
    print("2.Update data")
    print("3.Select data")
    print("4.Delete data")
    print("5.Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        NAME=input("Enter name: ")
        AGE = input("Enter age: ")
        GRADE = input("Enter grade: ")
        insert(NAME,AGE,GRADE)
    elif choice==2:
        ID = input("Enter id:")
        NAME = input("Enter name: ")
        AGE = input("Enter age: ")
        GRADE = input("Enter grade: ")
        update(NAME, AGE, GRADE,ID)
    elif choice==3:
        select()
    elif choice==4:
        ID = input("Enter id: ")
        delete(ID)
    elif choice==5:
        quit()
    else:
        print("Invalid selection, Please Try again..........")




