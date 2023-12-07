from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def DeleteDebit():
    import editdebit
    editdebit.run()
    return

def DeleteCredit():
    import editcredit
    editcredit.run()
    return

def AddDebit():
    import adddebit
    adddebit.run()
    return

def AddCredit():
    import addcredit
    addcredit.run()
    return

def Reports():
    root.destroy()
    import reports
    reports.run()
    return

def run(): 
    global root 
    root = Tk()
    root.geometry("600x400")
    root.resizable(False, False)
    bg = PhotoImage(file = "dashboard.png")
    l = Label(image = bg)
    l.pack()
    root.title("Dashboard")
    Label(root, text="Finance Management", fg="red", font=(None, 30)).place(x=125, y=10)
    
    Button(root, text="Delete/Edit Debit Transactions",command = DeleteDebit,height=3, width= 30).place(x=50, y=100)
    Button(root, text="Delete/Edit Credit Transactions",command = DeleteCredit,height=3, width= 30).place(x=350, y=100)
    Button(root, text="New Debit",command = AddDebit,height=3, width= 30).place(x=50, y=200)
    Button(root, text="New Credit",command = AddCredit,height=3, width= 30).place(x=350, y=200)
    Button(root, text="Finance Reports",command = Reports,height=3, width= 30).place(x=180, y=300)
     
    root.mainloop()
