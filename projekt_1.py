"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jakub Macura
email: kubamacura@email.cz
discord: Kuba1435#9487
"""

from task_template import TEXTS
from collections import Counter


#variables
number_control = True
test = True
count_of_login = {}
attempt = 2
sep = "-" * 41
count_of_num = list()
titlecase = list()
uppercase = list()
lowercase = list()
count_of_number = list()
sum_of_number = list()

Word_Len = []
i = 0
Table = []
Temp_Row = []
Graf = ""

#registration control
registered = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
while number_control:
    user_name = input("Please, enter your username: ")
    password = input("Please, enter your password: ")

    #if the entered data matches the offer
    if user_name in registered.keys() and password in registered.values():
        print(sep, f"Welcome to the app, {user_name}", "We have 3 texts to be analyzed.", sep, sep="\n")
        select = input("Enter a number between 1 and 3 to select: ")
        #checking the select number
        # if select is a number
        if select in ("1", "2", "3"):
            text = TEXTS[int(select) - 1]
            print(sep)
        # if select is not a number
        else:
            print("Please, choose from the selection")
            quit()
    #if user put wrong data matches
    else:
        count_of_login[user_name] = password
        #if user enter 2 incorrect attempts
        if len(count_of_login.keys()) == 2:
            print("Unregistered user, terminating the program...")
            quit()
        #if user enter incorrect attempt
        else:
            attempt = attempt - len(count_of_login.keys())
            print(f"Unregistered user. {attempt} attempts left")
            continue

    count_of_num = list()
    titlecase = list()
    uppercase = list()
    lowercase = list()
    count_of_number = list()

    for word in text.split():
        #count of words
        count_of_num.append(word)

        #count of titlecase
        if word.istitle():
            titlecase.append(word)

        #count of uppercase
        if word.isupper() and word.isalpha():
            uppercase.append(word)

        #count of lowercase
        if word.islower():
            lowercase.append(word)

        #count of all number
        if word.isnumeric():
            count_of_number.append(word)

        #sum of all numbers
        count = 0
        for num in count_of_number:
            if isinstance(num, str) and not num.isnumeric():
                continue
            count = count + int(num)

        Word_Len.append(len(word))

    for i in Counter(Word_Len).items():
        Table.append(i)
    Table.sort(key=lambda x: x[0], reverse=False)




    #statement of the calculation
    print(f"The are {len(count_of_num)} words in the selected text.")
    print(f"There are {len(titlecase)} titlecase words.")
    print(f"There are {len(uppercase)} uppercase words.")
    print(f"There are {len(lowercase)} lowercase words.")
    print(f"There are {len(count_of_number)} numeric strings.")
    print(f"The sum of all the numbers {count} ")

    print(sep, "LEN|  OCCURENCES  |NR.", sep, sep="\n")

    for row in range(len(Table)):
        print_row_len = ""
        Temp_Row = Table[row]
        Temp_Graf_Star = (len(Table)/14)
        Count_star = (int(Temp_Row[1]) * Temp_Graf_Star)

        for i in range(len(str(len(Table))) - (len(str(Temp_Row[0])))):
            print_row_len = print_row_len + " "
        print_row_len = print_row_len + str(Temp_Row[0])

        Graf = ""
        for i in range(14):
            if Count_star < i:
                Graf = Graf + " "
            else:
                Graf = Graf + "*"

        print_row_nr = Temp_Row[1]
        print(print_row_len, "|", Graf, "|", print_row_nr)
    number_control = False
    quit()