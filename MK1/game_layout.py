from tkinter import *
import MySQLdb
from MySQLdb import _mysql
import random


def game_screen():
    global choice_ID, question_Sen, choice1, choice2, choice3, choice4

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
    cursor.execute(f"select distinct qc.choice_id, q.question, qc.correct_choice, qc.choice1, "
                   f"qc.choice2, qc.choice3, qc.choice4 from question_choices qc inner join questions q "
                   f"on qc.question_id=q.question_id inner join question_category qct "
                   f"on qct.cat_id = qc.cat_id and q.cat_id = qc.cat_id where qc.cat_id=5;")
    # the genre category will go in brackets
    """    cursor.execute(f"select distinct qc.choice_id, q.question, qc.correct_choice, qc.choice1, "
                       f"qc.choice2, qc.choice3, qc.choice4 from question_choices qc inner join questions q "
                       f"on qc.question_id=q.question_id inner join question_category qct "
                       f"on qct.cat_id = qc.cat_id and q.cat_id = qc.cat_id"
                       f"where qc.cat_id={};" )"""

    info = cursor.fetchall()
    data = random.choice(info)

    # holds the question ID
    choice_ID = data[0]

    # holds the question sentence
    question_Sen = data[1]
    # correct choice
    correct_choice = data[2]
    # 4 options
    choice1 = data[3]
    choice2 = data[4]
    choice3 = data[5]
    choice4 = data[6]


    print(question_Sen, choice1,choice2,choice3, choice4)

    win = Tk()
    win.geometry("1200x800")
    win.config(bg='dark turquoise')

    username = StringVar()
    username_label = Label(win, textvariable=username, bg='white', width='20', height='3')
    username_label.grid(row=0, column=0, sticky=NW, padx=85)

    Label(win, text='Username:', height=3).grid(row=0, sticky=NW)

    question = StringVar()
    question.set(question_Sen)
    question_label = Label(win, textvariable=question, background='white', width='120', height='8', font=40)
    question_label.grid(row=0, columnspan=2, padx=120, pady=100)

    #Label(win, text='Question:', height=3).grid(row=0, sticky=W, padx=10)

    choice_1 = StringVar()
    choice_1.set(choice1)
    choice1 = Button(win, textvariable=choice_1, background='gray37', width=60, height='6', font=40, fg='dark turquoise')
    choice1.grid(row=1, column=0, sticky=E)

    choice_2 = StringVar()
    choice_2.set(choice2)
    choice2 = Button(win, textvariable=choice_2, bg='gray37', width=60, height='6',font=40, fg='dark turquoise')
    choice2.grid(row=1, column=1, sticky=W)

    choice_3 = StringVar()
    choice_3.set(choice3)
    choice3 = Button(win, textvariable=choice_3, bg='gray37', width=60, height='6',font=40, fg='dark turquoise')
    choice3.grid(row=2, column=0, sticky=E)

    choice_4 = StringVar()
    choice_4.set(choice4)
    choice4 = Button(win, textvariable=choice_4, bg='gray37', width=60, height='6',font=40, fg='dark turquoise')
    choice4.grid(row=2, column=1, sticky=W)

    win.mainloop()


if __name__ == '__main__':
    game_screen()