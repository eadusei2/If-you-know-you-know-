import MySQLdb
from MySQLdb import _mysql
from tkinter import *
import random
import json
import sys
import simpleaudio as sa
from playsound import playsound
import winsound
from winsound import SND_FILENAME,SND_ASYNC, SND_LOOP, PlaySound

start = list()
score = 0
repeat = 0


def correct_music():
    file = ['C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\Groovy Baby!.wav',
            'C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\Straight up 1x.wav',
            'C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\Talladega Nights, I piss excellence.wav',
            'C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\Travis Scott - It\'s Lit Soundbyte.wav',
            'C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\Travis Scott - Ya Ya Soundbyte.wav']

    song = random.choice(file)
    PlaySound(song, SND_FILENAME|SND_ASYNC)


def incorrect_music():
    file = ['C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\BOO YOU STINK  Spongebob Squarepants.wav',
            'C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\The A-team - MR T Quotes (2).wav',
            'C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\Yoda - That is why you fail.wav',
            'C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\You\'re killin me smalls!!.wav',
            'C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\Bishop Bullwinkle Hell To Da Naw,Naw,Naw With Da Bicycle.wav',
            'C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\Oh hell nah Sound Effect.wav']

    song = random.choice(file)
    PlaySound(song, SND_FILENAME|SND_ASYNC)


def background_music():
    file = ['C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\Academy Awards Original Music Theme.wav']

    winsound.PlaySound(file[0], winsound.SND_ASYNC | winsound.SND_ALIAS)


def game_music():
    file = ['C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\Academy Awards Original Music Theme1.wav']

    winsound.PlaySound(file[0], winsound.SND_ASYNC | winsound.SND_ALIAS)


def intro_music():
    file = ['C:\\Users\evans\OneDrive\Documents\CIS440_Game_music\Pusha T - If You Know You Know.wav']

    #for f in file:
    song = random.choice(file)
    PlaySound(song, SND_FILENAME|SND_LOOP|SND_ASYNC)


def exit():
    sys.exit()


def exit_screen():
    main_entry.destroy()


def exit_menu():
    """"""
    sys.exit()


def exit_game():
    gameScreen_Gui.destroy()


def log_on():
    global main_entry
    """"""
    # ----------------- login/registration screen ------
    main_entry = Tk()

    main_entry.geometry("1200x800")
    main_entry.title("If you know you know!!!")
    main_entry.configure(bg='gray37')

    # Form label
    Label(text="Login Or Register", bg="turquoise", width="200", height="2", font=("Calibri", 20)).pack()
    Label(text="", bg='gray37').pack()

    # login button
    Button(text="Login", height="8", width="80", command=login_screen).pack()
    Label(text="", bg='gray37').pack()

    # register button
    Button(text="Register", height="8", width="80", command=registration).pack()

    # exit button
    button = Button(text="Exit", height="4", width="20", command=exit)
    button.pack()

    intro_music()
    main_entry.mainloop()
    log_on()
    login_screen()
    game_menu()
    game_screen()
    incorrect()
    correct()


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
    cursor.execute(f"INSERT INTO user Values (4, '{user1}', '{passw1}',null,'{email1}',0);")
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

    login_gui.update()

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
    cursor.execute(f"SELECT username, password From user;")
    #cursor.execute(f"SELECT * From User WHERE username='{user}' AND password='{passw}';")

    data = cursor.fetchall()
    print(data)

    for d in data:
        checkU = d[0]
        checkp = d[1]

    if checkU == username_l.get() and checkp == password_l.get():
                Label(login_gui, text="'Successful login'", bg='gray37').pack()
                game_menu()
    elif checkU != username_l.get() or checkp != password_l.get():
                Label(login_gui, text="'Unsuccessful login'", bg='gray37').pack()

    db_connection.close()


def game_screen():
    global choice_ID, question_Sen, choice1, choice2, choice3, choice4, \
        choice_1, choice_2, choice_3, choice_4,correct_choice, gameScreen_Gui

    try:
        gameMenu_Gui.destroy()
    except:
        pass
    game_music()

    gameScreen_Gui = Toplevel()
    gameScreen_Gui.geometry("1200x800")
    gameScreen_Gui.config(bg='dark turquoise')

    if clicked.get() == 'Comedy':
        categoryOpp = '2'
    elif clicked.get() == 'Romance':
        categoryOpp = '3'
    elif clicked.get() == 'Thriller':
        categoryOpp = '4'
    elif clicked.get() == 'Action':
        categoryOpp = '5'
    print(categoryOpp)


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
    """    cursor.execute(f"select distinct qc.choice_id, q.question, qc.correct_choice, qc.choice1, "
                       f"qc.choice2, qc.choice3, qc.choice4 from question_choices qc inner join questions q "
                       f"on qc.question_id=q.question_id inner join question_category qct "
                       f"on qct.cat_id = qc.cat_id and q.cat_id = qc.cat_id where qc.cat_id=5;")"""
    # the genre category will go in brackets
    cursor.execute(f"select distinct qc.choice_id, q.question, qc.correct_choice, qc.choice1, "
                       f"qc.choice2, qc.choice3, qc.choice4 from question_choices qc inner join questions q "
                       f"on qc.question_id=q.question_id inner join question_category qct "
                       f"on qct.cat_id = qc.cat_id and q.cat_id = qc.cat_id where qc.cat_id={categoryOpp};")
    try:
        info = cursor.fetchall()
        with open('question.json', 'r') as file:
            test1 = json.load(file)

        for i in info:
            choice_ID = f'{i[0]}'
            question_Sen = f'{i[1]}'.strip()
            correct_choice = f'{i[2]}'.strip()
            choice1 = f'{i[3]}'.strip()
            choice2 = f'{i[4]}'.strip()
            choice3 = f'{i[5]}'.strip()
            choice4 = f'{i[6]}'.strip()

            test1 = [
                {"ID": choice_ID, "Question_ID": question_Sen, "correct_Choice": correct_choice, "choice1": choice1,
                 "choice2": choice2, "choice3": choice3, "choice4": choice4}]

            with open('question.json', 'w') as file:
                start_dict = {"QUESTIONS": test1}
                start.append(start_dict)

                run = json.dump(start, file, indent=3)

        with open('question.json', 'r') as file:
            test2 = json.load(file)

        data = random.choice(test2)
        print(data)

        question_Sen = data['QUESTIONS'][0]['Question_ID']
        correct_choice = data['QUESTIONS'][0]['correct_Choice']
        choice11 = data['QUESTIONS'][0]['choice1']
        choice22 = data['QUESTIONS'][0]['choice2']
        choice33 = data['QUESTIONS'][0]['choice3']
        choice44 = data['QUESTIONS'][0]['choice4']

        print(question_Sen, choice1, choice2, choice3, choice4)
    except (IOError, FileNotFoundError, TypeError, Exception) as ex:
        print(ex)
        pass
        """
            with open('question.json', 'r') as file:
                test2 = json.load(file)
                # data = random.choice(test2)
                # print(data)
        
            for t in test2:
                question_Sen = t['QUESTIONS'][0]['Question_ID']
                correct_choice = t['QUESTIONS'][0]['correct_Choice']
                choice1 = t['QUESTIONS'][0]['choice1']
                choice2 = t['QUESTIONS'][0]['choice2']
                choice3 = t['QUESTIONS'][0]['choice3']
                choice4 = t['QUESTIONS'][0]['choice4']
                t['QUESTIONS'][0]['Repeat'] = 1
"""
    # ------------------------------------------------------------------------------------------------------------------
    #username = StringVar()
    username_label = Label(gameScreen_Gui, textvariable=username_l, bg='white', width='20', height='3', font=15)
    username_label.grid(row=0, column=0, sticky=NW, padx=85)

    Label(gameScreen_Gui, text='Username:', height=3).grid(row=0, sticky=NW)

    question = StringVar()
    question.set(question_Sen)
    question_label = Label(gameScreen_Gui, textvariable=question, background='white', width='100', height='8', font=40)
    question_label.grid(row=0, columnspan=2, padx=120, pady=100)

    choice_1 = StringVar()
    choice_1.set(choice11)
    choice1 = Button(gameScreen_Gui, textvariable=choice_1, background='gray37', width=40, height='5',
                     font=30, fg='dark turquoise', command=correct_pick1)
    choice1.grid(row=1, column=0, sticky=E)

    choice_2 = StringVar()
    choice_2.set(choice22)
    choice2 = Button(gameScreen_Gui, textvariable=choice_2, bg='gray37', width=40, height='5',font=30,
                     fg='dark turquoise', command=correct_pick2)
    choice2.grid(row=1, column=1, sticky=W)

    choice_3 = StringVar()
    choice_3.set(choice33)
    choice3 = Button(gameScreen_Gui, textvariable=choice_3, bg='gray37', width=40, height='5',font=30,
                     fg='dark turquoise', command=correct_pick3)
    choice3.grid(row=2, column=0, sticky=E)

    choice_4 = StringVar()
    choice_4.set(choice44)
    choice4 = Button(gameScreen_Gui, textvariable=choice_4, bg='gray37', width=40, height='5', font=30,
                     fg='dark turquoise',command=correct_pick4)
    choice4.grid(row=2, column=1, sticky=W)

    exit1 = Button(gameScreen_Gui, text='Log Out', font=("Calibri", 12), height=2, width=10, command=exit_game)
    exit1.grid(row=0, column=1, sticky=NE, padx=85)

    gameScreen_Gui.update()

    with open('question_number.json', 'r') as file:
        exe = json.load(file)
        number = exe['question_num']

    question_number = {"question_num": number}
    question_number["question_num"] = question_number.get("question_num", 0) + 1

    with open('question_number.json', 'w') as file:
        save = json.dump(question_number, file)
        print(f'question_num: {save}')

    if question_number["question_num"] == 10:
        gameScreen_Gui.destroy()
        leaderboard()


def game_menu():
    global select_genre, log_out, game_button, categoryOpp, clicked, gameMenu_Gui

    login_gui.destroy()
    winsound.PlaySound(None, winsound.SND_ASYNC)
    background_music()

    gameMenu_Gui = Tk()
    gameMenu_Gui.geometry("1200x800")
    gameMenu_Gui.config(bg='dark turquoise')

    # Opening screen of program: homepage/menu page
    frame1 = Frame(gameMenu_Gui, bg='gray37')
    frame1.pack(side=TOP, anchor=E)

    frame2 = Frame(gameMenu_Gui, bg='gray37')
    frame2.place(x=0, y=0)

    frame3 = Frame(gameMenu_Gui, bg='gray37')
    frame3.pack(side=TOP, anchor=N)

    select_genre_label = Label(frame3, text='Select your genre:', font=("Calibri", 15), bg='gray37', fg='white')
    select_genre_label.pack()

    genres = ['Comedy', 'Romance', 'Thriller', 'Action']
    clicked = StringVar()
    clicked.set(genres[0])
    select_genre = OptionMenu(frame3, clicked, *genres)
    select_genre.config(width=10, height=1, font=("Calibri", 15))
    select_genre['menu'].config(font=("Calibri", 15))
    select_genre.pack()

    if clicked.get() == 'Comedy':
        categoryOpp = '2'
    elif clicked.get() == 'Romance':
        categoryOpp = '3'
    elif clicked.get() == 'Thriller':
        categoryOpp = '4'
    elif clicked.get() == 'Action':
        categoryOpp = '5'

    log_out = Button(frame1, text='Log Out', font=("Calibri", 10), height=1, width=8, command=exit_menu)
    log_out.pack(side=TOP, anchor=E, padx=10, pady=10)

    leaderboard_button = Button(frame2, text='Leaderboard', font=("Calibri", 10), height=1, width=12, command=leaderboard)
    leaderboard_button.pack(side=TOP, anchor=W, padx=10, pady=10)

    game_button = Button(gameMenu_Gui, text='PLAY GAME', font=("Calibri", 20), height=3, width=15, command=game_screen)
    game_button.pack(side=TOP, anchor=N, pady=200)

    gameMenu_Gui.update()


def leaderboard():

    leaderboard_gui = Tk()
    leaderboard_gui.geometry("1200x800")
    leaderboard_gui.config(bg='dark turquoise')

    frame1 = Frame(leaderboard_gui, bg='dark turquoise')
    frame1.pack(side=TOP, anchor=E)

    frame2 = Frame(leaderboard_gui, bg='dark turquoise')
    frame2.place(x=0, y=0)

    frame3 = Frame(leaderboard_gui)
    frame3.pack(side=TOP, anchor=N)

    leaderboard_label = Label(frame3, text='LEADERBOARD', bg='dark turquoise', fg='black')
    leaderboard_label.config(font="Calibri 30 underline")
    leaderboard_label.pack()

    exit_game = Button(frame1, text='Exit', font=("Calibri", 10), height=1, width=8, command=exit)
    exit_game.pack(side=TOP, anchor=E, padx=10, pady=10)

    return_button = Button(frame2, text='Return to Menu', font=("Calibri", 10), height=1, width=12, command=game_menu)
    return_button.pack(side=TOP, anchor=W, padx=10, pady=10)

    with open('score.json', 'r') as file:
        read = json.load(file)
        name = read['User']
        score3 = read['Score']
        total = f'{name} - {score3} Points'

    leaderboard_data = Listbox(leaderboard_gui, height=65, width=75, font=50)
    leaderboard_data.pack(side=TOP, anchor=N, pady=10)
    leaderboard_data.insert(1, total)
    leaderboard_gui.update()


def destroy1():
    okay.destroy()


def cor_destroy():
    correct12.destroy()


def incorrect():
    """ """
    incorrect_music()
    score = 0
    global okay

    okay = Tk()
    okay.geometry("1200x800")
    okay.config(bg='dark turquoise')

    Label(okay, text="That is incorrect! D:",fg='dark turquoise', height='3', bg='gray37', font=(None, 30)).grid(row=1, columnspan=2,
                                                                                            padx=480, pady=100)

    continue_btn = Button(okay, text='Continue', height='3', bg='gray37', command=lambda: [game_screen(), destroy1()])
    continue_btn.grid(row=2, sticky=SE)

    logout_btn = Button(okay, text='Logout', height='3', bg='gray37', command=log_on)
    logout_btn.grid(row=0, column=1, sticky=E)

    exit_btn = Button(okay, text='Exit', height='3', width='5', bg='gray37', command=exit_game)
    exit_btn.grid(row=0, column=0, sticky=W)

    okay.update()


def score1():
    score = 0
    final_score = {"User":username_l,"Score": score}
    final_score["Score"] += 20

    with open('score.json', 'w') as file:
        save = json.dump(final_score, file)
        print(f'Score: {save}')


def correct():
    """ """
    global correct12
    correct_music()
    name = f'{username_l.get()}'
    with open('score.json', 'r') as file:
        exe = json.load(file)
        score = exe['Score']
    final_score = {"User": name, "Score": score}
    final_score["Score"] = final_score.get("Score", 0) + 20

    with open('score.json', 'w') as file:
        save = json.dump(final_score, file)
        print(f'Score: {save}')

    correct12 = Tk()
    correct12.geometry("1200x800")
    correct12.config(bg='dark turquoise')

    Label(correct12, text="That is correct! :D", height='5', bg='gray37',fg='dark turquoise', font=(None, 30)).grid(row=1, columnspan=2, padx=480,
                                                                                          pady=100)
    continue_btn = Button(correct12, text='Continue', height='3', bg='gray37', command=lambda: [game_screen(), cor_destroy()])
    continue_btn.grid(row=2, sticky=SE)

    logout_btn = Button(correct12, text='Logout', height='3', bg='gray37', command=log_on)
    logout_btn.grid(row=0, column=1, sticky=E)

    exit_btn = Button(correct12, text='Exit', height='3', width='5', bg='gray37', command=exit_game)
    exit_btn.grid(row=0, column=0, sticky=W)
    correct12.update()


def correct_pick1():
    try:
        if choice_1.get() == correct_choice:
            print('Correct pick test complete')
            gameScreen_Gui.destroy()
            correct()

        elif choice_1.get() != correct_choice:
            print('wrong answer test complete')
            gameScreen_Gui.destroy()
            incorrect()
    except (EXCEPTION,Exception) as ex:
        pass


def correct_pick2():
    try:
        if choice_2.get() == correct_choice:
            print('Correct pick test complete')
            gameScreen_Gui.destroy()
            correct()

        elif choice_2.get() != correct_choice:
            print('wrong answer test complete')
            gameScreen_Gui.destroy()
            incorrect()
    except (EXCEPTION, Exception) as ex:
        pass


def correct_pick3():

    try:
        if choice_3.get() == correct_choice:
            print('Correct pick test complete')
            gameScreen_Gui.destroy()
            correct()

        elif choice_3.get() != correct_choice:
            print('wrong answer test complete')
            gameScreen_Gui.destroy()
            incorrect()
    except (EXCEPTION, Exception) as ex:
        pass


def correct_pick4():
    try:
        if choice_4.get() == correct_choice:
            print('Correct pick test complete')
            gameScreen_Gui.destroy()
            correct()

        elif choice_4.get() != correct_choice:
            print('wrong answer test complete')
            gameScreen_Gui.destroy()
            incorrect()
    except (EXCEPTION, Exception) as ex:
        pass


if __name__ == '__main__':
    log_on()