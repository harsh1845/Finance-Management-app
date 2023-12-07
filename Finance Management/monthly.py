import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime


def monthly():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="financemanagement")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,name,value,reason,moment FROM debit")
    records = mycursor.fetchall()
    now = datetime.now()
    moment_now = now.strftime("%d/%m/%Y %H:%M:%S")
    netdebit=0
    for i,(id,name,value,reason,moment) in enumerate(records, start=1):
        if(moment_now[3:10]==moment[3:10]):
            did='D'+str(id)
            netdebit+=value
            listBox.insert("", "end", values=(did,name,value,reason,moment))
    mysqldb.close()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="financemanagement")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,name,value,reason,moment FROM credit")
    records = mycursor.fetchall()
    netcredit=0
    for i, (id,name,value,reason,moment) in enumerate(records, start=1):
        if(moment_now[3:10]==moment[3:10]):
            cid='C'+str(id)
            netcredit+=value
            listBox.insert("", "end", values=(cid,name,value,reason,moment))
    e1.delete(0, END)
    e1.insert(END, netcredit)
    e2.delete(0, END)
    e2.insert(END, netdebit)
    mysqldb.close()


def run():
    root = Toplevel()
    root.geometry("1020x400")
    root.resizable(False, False)
    global bg
    bg = PhotoImage(file = "reports.png")
    l = Label(root,image = bg)
    l.grid()
    Label(root, text="Monthly Reports", fg="red", font=(None, 30)).place(x=400, y=20)
    cols = ('id', 'name', 'value','reason', 'datetime')
    global listBox
    listBox = ttk.Treeview(root, columns=cols, show='headings' )

    for col in cols:
        listBox.heading(col, text=col)

    listBox.grid(row=1, column=0, columnspan=1)
    listBox.place(x=10, y=100)
    global e1
    global e2
    Label(root, text="Net Credit").place(x=130, y=350)
    Label(root, text="Net Debit").place(x=530, y=350)

    e1 = Entry(root)
    e1.place(x=230, y=350)
 
    e2 = Entry(root)
    e2.place(x=630, y=350)
    monthly()
    root.mainloop()