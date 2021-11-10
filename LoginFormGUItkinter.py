#  GUI login form in tkinter using Sqlite3 database in Python3
#  Programmed by : Shahid


import sqlite3
from tkinter import*
from tkinter import messagebox
from sqlite3 import *                      # importing sqlite3 for database

conn = sqlite3.connect('login.db')

# creating cursor
c = conn.cursor()

# Creating a table for storing data
c.execute(
    'CREATE TABLE IF NOT EXISTS loginform(username TEXT, password TEXT)')
conn.commit()
conn.close()


def win4exit():
    win4.destroy()


def nextwindow():
    print("User Found")
    global win4
    win4 = Toplevel(root)
    win4.geometry("600x400")

    label4 = Label(win4, text="Hello there, Great to see you!", font=(
        "Arial", 25, "bold"), fg="black").pack(pady=60, fill=X)
    button4 = Button(win4, text="Exit", font=(
        "Monospace", 15, "bold"), width=10, command=win4exit, bg="red", fg="white").place(x=240, y=230)


def clear_form():
    sign_name.set("")
    sign_pass.set("")


def clear_register():
    register_name.set("")
    register_pass2.set("")
    register_pass.set("")


def get_sign_data():

    s = sign_name.get()
    s2 = sign_pass.get()
    y = (s, s2)
    if s == "" and s2 == "":
        messagebox.showinfo("warning", " Please fill the form")
        win3.destroy()
        opensignin()

    else:
        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        c.execute(
            "SELECT * FROM loginform where username = ? AND password = ?", y)
        row = c.fetchall()
        if row:
            nextwindow()
            # print("Username = ", s)
            # print("password = ", s2)
            win3.destroy()

        else:
            messagebox.showwarning('warning', 'User not found!')
            win3.destroy()
            opensignin()


def get_register_data():
    r11 = register_name.get()
    p11 = register_pass.get()
    p12 = register_pass2.get()

    # passing the entered data in a touple
    t = (r11, p11)

    if(r11 == "" and p11 == "" and p12 == ""):
        messagebox.showinfo("Warning!", " Please fill the form")
        win2.destroy()
        openregister()

    elif(p11 != p12):
        messagebox.showwarning("Warning!", "Password didn't match")

    else:

        # creating database connection and registering new user
        conn = sqlite3.connect('login.db')

        # creating cursor
        c = conn.cursor()

        # Creating a table for storing data
        c.execute(
            'CREATE TABLE IF NOT EXISTS loginform(username TEXT, password TEXT)')

        # Inserting data in table
        conn.execute(
            'INSERT INTO loginform(username,password) VALUES(?,?)', t)
        conn.commit()
        conn.close()
        messagebox.showinfo("register", "User Added sccessfully")
        win2.destroy()
        # print("Username = ", r11)
        # print("Password = ", p12)


def openregister():
    global win2
    win2 = Toplevel(root)
    win2.geometry("650x400")
    win2.title("Register User")
    win2.iconbitmap(r"avataricon.ico")
    win2.resizable(False, False)

    heading2 = Label(win2, text="Register New User", bg="black",
                     font=("Arial", 14, "bold"), width=20, fg="white", bd=4)
    heading2.grid(row=0, column=1, pady=10, sticky="w")

    namelbl2 = Label(win2, text="Enter Username", font=(
        "monospace", 12, "bold")).grid(pady=10, row=1, column=0, padx=20)
    passlb2 = Label(win2, text="Enter Password", font=("monospace", 12, "bold")) .grid(
        pady=10, row=2, column=0, padx=20)
    passlb21 = Label(win2, text="Re-enter Password", font=("monospace", 12, "bold")) .grid(
        pady=10, row=3, column=0, padx=20)

    global register_name
    global register_pass
    global register_pass2

    register_name = StringVar()
    register_pass = StringVar()
    register_pass2 = StringVar()

    register_name_entry = Entry(win2, textvariable=register_name, font=(
        "monospace", 12, "bold"), width=30).grid(row=1, column=1, padx=10)
    register_pass_entry = Entry(win2, textvariable=register_pass, show="*", font=(
        "monospace", 12, "bold"), width=30).grid(row=2, column=1, padx=10)
    register_pass_entry2 = Entry(win2, textvariable=register_pass2, show="*", font=(
        "monospace", 12, "bold"), width=30).grid(row=3, column=1, padx=10)

    submitbtn2 = Button(win2, text="Submit", font=(
        "Arial", 14, "bold"), bg="green", fg="white", command=get_register_data).place(x=220, y=260)

    clearbtn2 = Button(win2, text="clear", font=(
        "Arial", 14, "bold"), bg="red", fg="white", command=clear_register).place(x=380, y=260)


def rootexit():
    root.destroy()


def opensignin():
    global win3
    win3 = Toplevel(root)
    win3.geometry("600x300")
    win3.title("Sign in")
    win3.iconbitmap(r"avataricon.ico")
    win3.resizable(False, False)

    heading3 = Label(win3, text="Sign in", bg="black",
                     font=("Arial", 14, "bold"), width=10, fg="white", bd=4)
    heading3.grid(row=0, column=1, pady=10, padx=120, sticky="w")

    namelbl2 = Label(win3, text="Username", font=(
        "monospace", 13, "bold")).grid(pady=10, row=1, column=0, padx=20)
    passlb2 = Label(win3, text="Password", font=("monospace", 13, "bold")) .grid(
        pady=10, row=2, column=0, padx=20)

    global sign_name
    global sign_pass
    sign_name = StringVar()
    sign_pass = StringVar()

    sign_name_entry = Entry(win3, textvariable=sign_name, font=(
        "monospace", 12, "bold"), width=30).grid(row=1, column=1, padx=10)
    sign_pass_entry = Entry(win3, textvariable=sign_pass, show="*", font=(
        "monospace", 12, "bold"), width=30).grid(row=2, column=1, padx=10)

    submitbtn3 = Button(win3, text="Submit", font=(
        "Arial", 14, "bold"), bg="green", fg="white", command=get_sign_data).place(x=220, y=200)

    clearbtn3 = Button(win3, text="clear", font=(
        "Arial", 14, "bold"), bg="red", fg="white", command=clear_form).place(x=380, y=200)


# Creating main window
root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root["bg"] = "grey"
root.title("Sign-in/Register App by Shahid")

label1 = Label(root, text="Welcome To Our Page", bg="black",
               fg="white", font=("monospace", 20, "bold"), width=40, bd=4, relief=RIDGE).pack(side=TOP, fill=X)

button1 = Button(root, text="Sign in", font=(
    "Monospace", 15, "bold"), command=opensignin, bg="dark blue", fg="white", width=9).place(x=340, y=300)
button2 = Button(root, text="New User? Register", font=(
    "Monospace", 14, "bold"), command=openregister, bg="green", fg="white").place(x=85, y=302)

button31 = Button(root, text="Exit", font=(
    "Monospace", 15, "bold"), command=rootexit, bg="red", fg="white", width=7).place(x=500, y=300)

# for icon
root.iconbitmap(r"avataricon.ico")

photo = PhotoImage(file="avatar.png")
imagelabel = Label(image=photo).pack(pady=20)

root.mainloop()
