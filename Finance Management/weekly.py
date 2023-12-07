import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import time
import datetime

def weekly():
    WEEK=datetime.datetime.now().isocalendar()[1]
    WEEK=WEEK-1
    startdate = time.asctime(time.strptime('2023 %d 0' % WEEK, '%Y %W %w')) 
    startdate = datetime.datetime.strptime(startdate, '%a %b %d %H:%M:%S %Y') 
    dates = [startdate.strftime('%d/%m/%Y')]
    for i in range(1, 7): 
        day = startdate + datetime.timedelta(days=i)
        dates.append(day.strftime('%d/%m/%Y'))  

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="financemanagement")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,name,value,reason,moment FROM debit")
    records = mycursor.fetchall()
    netdebit=0
    for d in dates:
        for i,(id,name,value,reason,moment) in enumerate(records, start=1):
            if(d==moment[0:10]):
                did='D'+str(id)
                netdebit+=value
                listBox.insert("", "end", values=(did,name,value,reason,moment)) 
    mysqldb.close()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="financemanagement")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,name,value,reason,moment FROM credit")
    records = mycursor.fetchall()
    netcredit=0
    for d in dates:
        for i,(id,name,value,reason,moment) in enumerate(records, start=1):
            if(d==moment[0:10]):
                did='C'+str(id)
                netcredit+=value
                listBox.insert("", "end", values=(did,name,value,reason,moment)) 
    mysqldb.close()
    e1.delete(0, END)
    e1.insert(END, netcredit)
    e2.delete(0, END)
    e2.insert(END, netdebit)
    return
    


def run():
    root = Toplevel()
    root.geometry("1020x400")
    root.resizable(False, False)
    global bg
    bg = PhotoImage(file = "reports.png")
    l = Label(root,image = bg)
    l.grid()
    Label(root, text="Weekly Reports", fg="red", font=(None, 30)).place(x=400, y=20)
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
    weekly()
    
    root.mainloop()


    