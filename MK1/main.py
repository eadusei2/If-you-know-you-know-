import MySQLdb
from MySQLdb import _mysql
from tkinter import *


def exit_screen():
    main_entry.destroy()


def log_on():
    global main_entry
    """"""
    # ----------------- login/registration screen ------
    main_entry = Tk()

    main_entry.geometry("1200x800")
    main_entry.title("If you know you know!!!")
    main_entry.configure(bg='gray37')

    # Form label
    Label(text="Login Or Register", bg="dark turquoise", width="200", height="2", font=("Calibri", 20)).pack()
    Label(text="", bg='gray37').pack()

    # login button
    Button(text="Login", height="8", width="80", command=login_screen).pack()
    Label(text="", bg='gray37').pack()

    # register button
    Button(text="Register", height="8", width="80", command=registration).pack()

    # exit button
    button = Button(text="Exit", height="4", width="20", command=exit_screen)
    button.pack()

    main_entry.mainloop()
    log_on()
    login_screen()


def registration():
    global username, password, username_entry, password_entry, email_entry, email, registration_gui
    registration_gui = Toplevel(main_entry)
    registration_gui.title("Registration")
    registration_gui.geometry("600x350")
    registration_gui.configure(bg='gray37')

    username = StringVar()
    password = StringVar()
    email = StringVar()

    Label(registration_gui, text="Please enter your information", bg="turquoise", width=100, height=2).pack()
    Label(registration_gui, text="", bg='gray37').pack()

    email_lable = Label(registration_gui, text="Email")
    email_lable.pack()

    email_entry = Entry(registration_gui, textvariable=email, width=40)
    email_entry.pack()

    username_lable = Label(registration_gui, text="Username")
    username_lable.pack()

    username_entry = Entry(registration_gui, textvariable=username, width=40)
    username_entry.pack()

    # space between username and password
    Label(registration_gui, text="", bg='gray37').pack()

    # Set password label
    password_lable = Label(registration_gui, text="Password")
    password_lable.pack()

    # Set password entry
    password_entry = Entry(registration_gui, textvariable=password, width=40)
    password_entry.pack()

    Label(registration_gui, text="", bg='gray37').pack()

    # Set register button
    Button(registration_gui, text="Register", width=20, height=2, command=register_authentication).pack()

    # exit button
    button1 = Button(registration_gui, text="Exit", height="2", width="10", command=exit_screen)
    button1.pack()

    # --------------------------------------------------------------------------------------------


def register_authentication():
    global user1, passw1, checkU, checkp, email1

    try:
        user1 = username.get()
        passw1 = password.get()
        email1 = email.get()

        password_entry.delete(0, END)
        username_entry.delete(0, END)
        email_entry.delete(0, END)

    except:
        pass

    try:
        db_connection = MySQLdb.connect("107.180.1.16", "lascoronas", "!!Lascoronas", "lascoronas")
        # If connection is not successful
    except:
        print("Can't connect to database")
        return 0
    # If Connection Is Successful
    print("Connected")

    # Making Cursor Object For Query Execution
    cursor = db_connection.cursor()

    # Executing Query
    cursor.execute(f"INSERT INTO User Values (4, '{user1}', '{passw1}',null,'{email1}',0);")
    Label(registration_gui, text="'Successful Registration'", bg='gray37').pack()

    data = cursor.fetchall()
    print(data)

    db_connection.close()


def login_screen():
    global username_l, password_l, password_entry_l, username_entry_l, login_gui

    login_gui = Toplevel(main_entry)
    login_gui.title("Login")
    login_gui.geometry("600x350")
    login_gui.configure(bg='gray37')

    username_l = StringVar()
    password_l = StringVar()

    Label(login_gui, text="Please enter your information", bg="turquoise", width=100, height=2).pack()
    Label(login_gui, text="", bg='gray37').pack()

    username_lable = Label(login_gui, text="Username")
    username_lable.pack()

    username_entry = Entry(login_gui, textvariable=username_l, width=40)
    username_entry.pack()

    # space between username and password
    Label(login_gui, text="", bg='gray37').pack()

    # Set password label
    password_lable = Label(login_gui, text="Password")
    password_lable.pack()

    # Set password entry
    password_entry = Entry(login_gui, textvariable=password_l, width=40)
    password_entry.pack()

    Label(login_gui, text="", bg='gray37').pack()

    # Set register button
    Button(login_gui, text="Login", width=20, height=2, command=login_authentication).pack()
    Label(login_gui, text="", bg='gray37').pack()

    # exit button
    button1 = Button(login_gui, text="Exit", height="2", width="10", command=exit_screen)
    button1.pack()

    # -----------------------------------------------------------------------------------------


def login_authentication():
    global user, passw, checkU, checkp

    try:
        user = username_l.get()
        passw = password_l.get()

        password_entry_l.delete(0, END)
        username_entry_l.delete(0, END)
    except:
        pass

    try:
        db_connection = MySQLdb.connect("107.180.1.16", "lascoronas", "!!Lascoronas", "lascoronas")
        # If connection is not successful
    except:
        print("Can't connect to database")
        return 0
    # If Connection Is Successful
    print("Connected")

    # Making Cursor Object For Query Execution
    cursor = db_connection.cursor()

    # Executing Query
    cursor.execute(f"SELECT username, password From User;")
    #cursor.execute(f"SELECT * From User WHERE username='{user}' AND password='{passw}';")

    data = cursor.fetchall()
    print(data)

    for d in data:
        checkU = d[0]
        checkp = d[1]

    if checkU == username_l.get() and checkp == password_l.get():
                Label(login_gui, text="'Successful login'", bg='gray37').pack()
    elif checkU != username_l.get() or checkp != password_l.get():
                Label(login_gui, text="'Unsuccessful login'", bg='gray37').pack()

    db_connection.close()




if __name__ == '__main__':
    log_on()
