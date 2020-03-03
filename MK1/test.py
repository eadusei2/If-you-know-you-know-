with open('question.json', 'r') as file:
    test2 = json.load(file)
    # data = random.choice(test2)
    # print(data)

for t in test2:
    question_Sen = t[0]
    correct_choice = t[1]
    choice1 = t[2]
    choice2 = t[3]
    choice3 = t[4]
    choice4 = t[5]
    t[6] = 1

    with open('question.json', 'w') as file:
        json.dump(t, file, indent=3)