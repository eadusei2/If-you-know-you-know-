# Github sucks balls

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
    button = Button(text="Exit", height="4", width="20",command=exit_screen)
    button.pack()

    main_entry.mainloop()
    log_on()
    login_screen()


def registration():

    registration_gui = Toplevel(main_entry)
    registration_gui.title("Registration")
    registration_gui.geometry("600x350")
    registration_gui.configure(bg='gray37')

    username = StringVar()
    password = StringVar()

    Label(registration_gui, text="Please enter your information", bg="turquoise", width=100, height=2).pack()
    Label(registration_gui, text="", bg='gray37').pack()

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
    Button(registration_gui, text="Register", width=20, height=2).pack()

    # exit button
    button1 = Button(registration_gui,text="Exit", height="2", width="10", command=exit_screen)
    button1.pack()

    # --------------------------------------------------------------------------------------------


def login_screen():
        global username_verify, password_verify

        login_gui = Toplevel(main_entry)
        login_gui.title("Login")
        login_gui.geometry("600x350")
        login_gui.configure(bg='gray37')

        username = StringVar()
        password = StringVar()

        Label(login_gui, text="Please enter your information", bg="turquoise", width=100, height=2).pack()
        Label(login_gui, text="", bg='gray37').pack()

        username_lable = Label(login_gui, text="Username")
        username_lable.pack()

        username_entry = Entry(login_gui, textvariable=username, width=40)
        username_entry.pack()

        # space between username and password
        Label(login_gui, text="", bg='gray37').pack()

        # Set password label
        password_lable = Label(login_gui, text="Password")
        password_lable.pack()

        # Set password entry
        password_entry = Entry(login_gui, textvariable=password, width=40)
        password_entry.pack()

        Label(login_gui, text="", bg='gray37').pack()

        # Set register button
        Button(login_gui, text="Login", width=20, height=2).pack()

        # exit button
        button1 = Button(login_gui, text="Exit", height="2", width="10", command=exit_screen)
        button1.pack()

        # -----------------------------------------------------------------------------------------


if __name__ == '__main__':
    log_on()
