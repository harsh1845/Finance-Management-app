import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def Search():
    debitid = e1.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="financemanagement")
    mycursor = mysqldb.cursor()
    sql = "SELECT id,name,value,reason FROM credit where id = %s"
    val = (debitid,)
    mycursor.execute(sql, val)
    records = mycursor.fetchall()
    for i, (id,name,value,reason) in enumerate(records, start=1):
        e2.delete(0, END)
        e2.insert(END, name)
        e3.delete(0, END)
        e3.insert(END, value)
        e4.delete(0, END)
        e4.insert(END, reason)
        e1.focus_set()
    return

def Update():
    tid = e1.get()
    name = e2.get()
    value = e3.get()
    reason = e4.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="financemanagement")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "Update  credit set name= %s,value= %s,reason= %s where id= %s"
       val = (name,value,reason,tid)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updateddddd successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
    return

def Delete():
    debitid = e1.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="financemanagement")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "delete from credit where id = %s"
       val = (debitid,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleteeeee successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
    return

def run(): 
    global root 
    root = Toplevel()
    root.geometry("600x400")
    root.resizable(False, False)
    global bg
    bg = PhotoImage(file = "all.png")
    l = Label(root,image = bg)
    l.pack()
    root.title("Edit/Delete a Credit Transaction")
    Label(root, text="Finance Management", fg="red", font=(None, 30)).place(x=125, y=10)
    
    global e1
    global e2
    global e3
    global e4
    Label(root, text="Transaction id").place(x=50, y=100)
    e1 = Entry(root)
    e1.place(x=150, y=100)
    Button(root, text="Search",command = Search,height=1, width= 10).place(x=300, y=100)
    

    Label(root, text="Name").place(x=150, y=200)
    Label(root, text="Value").place(x=150, y=250)
    Label(root, text="Reason").place(x=150, y=300)
    e2 = Entry(root)
    e2.place(x=200, y=200)
     
    e3 = Entry(root)
    e3.place(x=200, y=250)
     
    e4 = Entry(root)
    e4.place(x=200, y=300)

    Button(root, text="Delete Transaction",command = Delete,height=1, width= 20).place(x=50, y=350)
    Button(root, text="Update Transaction",command = Update,height=1, width= 20).place(x=350, y=350)
    root.mainloop()