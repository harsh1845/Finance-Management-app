from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import mysql.connector

def submit():
	name = e1.get()
	value = e2.get()
	reason = e3.get()
	mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="financemanagement")
	mycursor=mysqldb.cursor()
	now = datetime.now()
	moment = now.strftime("%d/%m/%Y %H:%M:%S")
	try:
		sql = "INSERT INTO  credit (name,value,reason,moment) VALUES (%s, %s, %s, %s)"
		val = (name,value,reason,moment)
		mycursor.execute(sql, val)
		mysqldb.commit()
		lastid = mycursor.lastrowid
		messagebox.showinfo("information", "Transaction inserted successfully...")
		e1.delete(0, END)
		e2.delete(0, END)
		e3.delete(0, END)
		e1.focus_set()
	except Exception as e:
		print(e)
		mysqldb.rollback()
		mysqldb.close()
	return

def run(): 
    root = Toplevel()
    root.geometry("300x250")
    root.resizable(False, False)
    global bg
    bg = PhotoImage(file = "all.png")
    l = Label(root,image = bg)
    l.pack()
    root.title("Add Credit Transaction")
    global e1
    global e2
    global e3
     
    Label(root, text="Add Credit", fg="black", font=(None, 24)).place(x=80, y=5)
     
    Label(root, text="Name").place(x=10, y=80)
    Label(root, text="Value (in rupees)").place(x=10, y=110)
    Label(root, text="Reason").place(x=10, y=140)
    Button(root, text="Submit",command = submit,height=1, width= 20).place(x=80, y=170)

    e1 = Entry(root)
    e1.place(x=140, y=80)
     
    e2 = Entry(root)
    e2.place(x=140, y=110)
     
    e3 = Entry(root)
    e3.place(x=140, y=140)
    root.mainloop()

