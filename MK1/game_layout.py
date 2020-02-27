from tkinter import *

win = Tk()
win.geometry("1200x800")
win.config(bg='dark turquoise')

username = StringVar()
username_label = Label(win, textvariable=username, bg='white', width='20', height='1')
username_label.grid(row=0, column=0, sticky=NW, padx=85)

Label(win, text='Username:', height=1).grid(row=0, sticky=NW)

question = StringVar()
question_label = Label(win, textvariable=question, background='white', width='100', height='5')
question_label.grid(row=0, columnspan=2, padx=120, pady=100)

Label(win, text='Question:').grid(row=0, sticky=W, padx=10)

answer = StringVar()
answer_1 = Button(win, textvariable=answer, background='gray37', width=40, height='4')
answer_1.grid(row=1, column=0, sticky=E)

answer2 = StringVar()
answer_2 = Button(win, textvariable=answer2, bg='gray37', width=40, height='4')
answer_2.grid(row=1, column=1, sticky=W)

answer3 = StringVar()
answer_3 = Button(win, textvariable=answer3, bg='gray37', width=40, height='4')
answer_3.grid(row=2, column=0, sticky=E)

answer4 = StringVar()
answer_4 = Button(win, textvariable=answer4, bg='gray37', width=40, height='4')
answer_4.grid(row=2, column=1, sticky=W)

win.mainloop()
