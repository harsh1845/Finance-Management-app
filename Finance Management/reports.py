from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def DailyLogs():
    import daily
    daily.run()
    return

def WeeklyLogs():
    import weekly
    weekly.run()
    return

def MonthlyLogs():
    import monthly
    monthly.run()
    return

def YearlyLogs():
    import yearly
    yearly.run()
    return

def Home():
    root.destroy()
    import dashboard
    dashboard.run()
    return

def run():
    global root 
    root = Tk()
    root.geometry("600x400")
    root.resizable(False, False)
    bg = PhotoImage(file = "dashboard.png")
    l = Label(image = bg)
    l.pack()
    root.title("Reports")
    Label(root, text="Finance Management", fg="red", font=(None, 30)).place(x=125, y=10)
    
    Button(root, text="Daily Logs",command = DailyLogs,height=3, width= 30).place(x=50, y=100)
    Button(root, text="Weekly Logs",command = WeeklyLogs,height=3, width= 30).place(x=350, y=100)
    Button(root, text="Monthly Logs",command = MonthlyLogs,height=3, width= 30).place(x=50, y=200)
    Button(root, text="Yearly Logs",command = YearlyLogs,height=3, width= 30).place(x=350, y=200)
    Button(root, text="Go Back",command = Home,height=2, width= 20).place(x=190, y=300)
    root.mainloop()
