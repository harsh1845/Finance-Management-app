import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def show():
	user = e1.get()
	passw = e2.get()
	#print(user, passw)
	mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="financemanagement")
	mycursor = mysqldb.cursor()
	mycursor.execute("SELECT * FROM users")
	records = mycursor.fetchall()
	flag=0
	for i in records:
		if(i[1]==user and i[2]==passw):
			flag=1
			root.destroy()
			import dashboard
			dashboard.run()
	if(flag==0):
		messagebox.showinfo("information","Invalid Login Details")
		
	


root = Tk()
root.geometry("800x300")
root.resizable(False, False)
root.title("Login")
bg = PhotoImage(file = "Login.png")
l = Label(image = bg)
l.pack()
Label(root, text="Finance Management", fg="red", font=(None, 30)).place(x=200, y=5)
global e1
global e2

Label(root, text="Username").place(x=230, y=100)
Label(root, text="Password").place(x=230, y=150)

e1 = Entry(root)
e1.place(x=360, y=100)
 
e2 = Entry(root)
e2.place(x=360, y=150)

Button(root, text="Login",command = show,height=1, width= 13).place(x=340, y=200)

root.mainloop()