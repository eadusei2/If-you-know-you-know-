from tkinter import *


def log_on():
    global main_entry
    """"""
# ----------------- login/registration screen ------
    main_entry = Tk()

    main_entry.geometry("1200x800")
    main_entry.title("Account Login")
    main_entry.configure(bg='gray37')

    # Form label
    Label(text="Login Or Register", bg="dark turquoise", width="200", height="2", font=("Calibri", 20)).pack()
    Label(text="").pack()

    # login button
    Button(text="Login", height="8", width="80").pack()
    Label(text="").pack()

    # register button
    Button(text="Register", height="8", width="80", command=registration).pack()

    main_entry.mainloop()
    log_on()


def registration():

    registration_gui = Toplevel(main_entry)
    registration_gui.title("Registration")
    registration_gui.geometry("600x350")

    username = StringVar()
    password = StringVar()

    Label(registration_gui, text="Please enter your information", bg="turquoise").pack()
    Label(registration_gui, text="").pack()

    username_lable = Label(registration_gui, text="Username")
    username_lable.pack()

    username_entry = Entry(registration_gui, textvariable=username, width=40)
    username_entry.pack()

    # Set password label
    password_lable = Label(registration_gui, text="Password")
    password_lable.pack()

    # Set password entry
    password_entry = Entry(registration_gui, textvariable=password, width=40)
    password_entry.pack()

    Label(registration_gui, text="").pack()

    # Set register button
    Button(registration_gui, text="Register", width=20, height=2, bg="turquoise").pack()


log_on()