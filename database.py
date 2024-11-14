import pymysql
from tkinter import messagebox




def connect_database():
    global conn, mycursor
    try:
        conn=pymysql.connect(host="localhost",user="root",password="shyam@8764")
        mycursor=conn.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS rr")
        mycursor.execute("USE  rr")
        mycursor.execute("CREATE TABLE IF NOT EXISTS ino(id int,Name varchar(20),Phone BIGINT,Role varchar(20),Gender varchar(20),Salary DECIMAL(10,2))")
        messagebox.showinfo("Succesfull","Your database is successfully created")
    except:
        messagebox.showerror("Error","Something went wrong ,Please open mysql app before running again")
    return
   




def insert(id, Name, Phone, Role, Gender, Salary):
    # Ensure `mycursor` and `conn` are correctly defined in the scope
    mycursor.execute("INSERT INTO ino VALUES (%s, %s, %s, %s, %s, %s)", (id, Name, Phone, Role, Gender, Salary))
    conn.commit()
def id_exists(id):
    mycursor.execute("SELECT COUNT(*) from ino where id=%s",id)
    result=mycursor.fetchone()
    return result[0]>0


def fetch_employees():
    mycursor.execute("select * from ino")
    result=mycursor.fetchall()
    return result

def update(id,New_Name,new_Phone,new_Role,new_Gender,new_Salary):
    mycursor.execute("UPDATE ino SET name=%s,Phone=%s,Role=%s,Gender=%s,Salary=%s WHERE id=%s",(New_Name,new_Phone,new_Role,new_Gender,new_Salary,id))
    conn.commit()



def delete(id):
    mycursor.execute("DELETE FROM ino where id=%s",id)

def Search(option,value):
    mycursor.execute(f"Select * from ino where {option}=%s",value)
    result=mycursor.fetchall()
    return result

def deleteall_records():
    mycursor.execute("TRUNCATE Table ino")
    conn.commit()


connect_database()
