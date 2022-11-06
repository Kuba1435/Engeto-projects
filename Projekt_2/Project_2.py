"""
Project_2.py: druhý projekt do Engeto Online Python Akademie
author: Jakub Macura
email: kubamacura@email.cz
discord: Kuba1435#9487
"""

# import
from traceback import print_stack
from sqlitedict import SqliteDict
import random
import time

# variables
sep = "-" * 58
double_sep = "=" * 58
game = "Bulls&Cows | Tic-tac-toe"
attempt = 0
cows = 0
bulls = 0
game_round = 0
Bulls_Cows_round_list = list()
Tic_tac_toe_round_list = list()
code = random.sample(range(1, 9), 4)
login_data = SqliteDict("login_data.data", autocommit=True)

board1 = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]

board3x3 = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]

board2 = ["-", "-", "-", "-", "-", "-",
            "-", "-", "-", "-", "-", "-",
            "-", "-", "-", "-", "-", "-",
            "-", "-", "-", "-", "-", "-",
            "-", "-", "-", "-", "-", "-",
            "-", "-", "-", "-", "-", "-"]

board6x6 = ["-", "-", "-", "-", "-", "-",
            "-", "-", "-", "-", "-", "-",
            "-", "-", "-", "-", "-", "-",
            "-", "-", "-", "-", "-", "-",
            "-", "-", "-", "-", "-", "-",
            "-", "-", "-", "-", "-", "-"]

currentPlayer = "X"
winner = None
GameRunning = True

# definition

## Tic-tac-toe

# game board
def gameBoard3x3(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def gameBoard6x6(board):
    print(board[0] + " | " + board[1] + " | " + board[2] + " | " + board[3] + " | " + board[4]
          + " | " + board[5])

    print("---------------------")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | " + board[9] + " | " + board[10]
          + " | " + board[11])

    print("---------------------")
    print(board[12] + " | " + board[13] + " | " + board[14] + " | " + board[15] + " | " + board[16]
          + " | " + board[17])

    print("---------------------")
    print(board6x6[18] + " | " + board[19] + " | " + board[20] + " | " + board[21] + " | " + board[22]
          + " | " + board[23])

    print("---------------------")
    print(board[24] + " | " + board[25] + " | " + board[26] + " | " + board[27] + " | " + board[28]
          + " | " + board[29])

    print("---------------------")
    print(board[30] + " | " + board[31] + " | " + board[32] + " | " + board[33] + " | " + board[34]
          + " | " + board[35])

# take player input
def pInput3x3(board):
    print(double_sep)
    inp = int(input(f"Player {currentPlayer} | Please enter your move number: "))
    print(double_sep)
    if board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print("This spot is already taken!")

def pInput6x6(board):
    print(double_sep)
    inp = int(input(f"Player {currentPlayer} | Please enter your move number: "))
    print(double_sep)
    if board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print("This spot is already taken!")
        print(sep, "", sep="\n")

# check for win or tie
def checkHorizontle3x3(board):
    global winner
    # row 1
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    # row 2
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    # row 3
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkHorizontle6x6(board):
    global winner

    # row 1
    if board[0] == board[1] == board[2] == board[3] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[2] == board[3] == board[4] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[3] == board[4] == board[5] and board[2] != "-":
        winner = board[2]
        return True

    # row 2
    elif board[6] == board[7] == board[8] == board[9] and board[6] != "-":
        winner = board[6]
        return True
    elif board[7] == board[8] == board[9] == board[10] and board[7] != "-":
        winner = board[7]
        return True
    elif board[8] == board[9] == board[10] == board[11] and board[8] != "-":
        winner = board[8]
        return True

    # row 3
    elif board[12] == board[13] == board[14] == board[15] and board[12] != "-":
        winner = board[12]
        return True
    elif board[13] == board[14] == board[15] == board[16] and board[13] != "-":
        winner = board[13]
        return True
    elif board[14] == board[15] == board[16] == board[17] and board[14] != "-":
        winner = board[14]
        return True

    # row 4
    elif board[18] == board[19] == board[20] == board[21] and board[18] != "-":
        winner = board[18]
        return True
    elif board[19] == board[20] == board[21] == board[22] and board[19] != "-":
        winner = board[19]
        return True
    elif board[20] == board[21] == board[22] == board[23] and board[20] != "-":
        winner = board[20]
        return True

    # row 5
    elif board[24] == board[25] == board[26] == board[27] and board[24] != "-":
        winner = board[24]
        return True
    elif board[25] == board[26] == board[27] == board[28] and board[25] != "-":
        winner = board[25]
        return True
    elif board[26] == board[27] == board[28] == board[29] and board[26] != "-":
        winner = board[26]
        return True

    # row 6
    elif board[30] == board[31] == board[32] == board[33] and board[30] != "-":
        winner = board[30]
        return True
    elif board[31] == board[32] == board[33] == board[34] and board[31] != "-":
        winner = board[31]
        return True
    elif board[32] == board[33] == board[34] == board[35] and board[32] != "-":
        winner = board[32]
        return True

def checkVerticale3x3(board):
    global winner

    # column 1
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    # column 2
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    # column 3
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True

def checkVerticale6x6(board):
    global winner

    # column 1
    if board[0] == board[6] == board[12] == board[18] and board[0] != "-":
        winner = board[0]
        return True
    elif board[6] == board[12] == board[18] == board[24] and board[6] != "-":
        winner = board[6]
        return True
    elif board[12] == board[18] == board[24] == board[30] and board[12] != "-":
        winner = board[12]
        return True

    # column 2
    elif board[1] == board[7] == board[13] == board[19] and board[1] != "-":
        winner = board[1]
        return True
    elif board[7] == board[13] == board[19] == board[25] and board[7] != "-":
        winner = board[7]
        return True
    elif board[13] == board[19] == board[25] == board[31] and board[13] != "-":
        winner = board[13]
        return True

    # column 3
    elif board[2] == board[8] == board[14] == board[20] and board[2] != "-":
        winner = board[2]
        return True
    elif board[8] == board[14] == board[20] == board[26] and board[8] != "-":
        winner = board[8]
        return True
    elif board[14] == board[20] == board[26] == board[32] and board[14] != "-":
        winner = board[14]
        return True

    # column 4
    elif board[3] == board[9] == board[15] == board[21] and board[3] != "-":
        winner = board[3]
        return True
    elif board[9] == board[15] == board[21] == board[27] and board[9] != "-":
        winner = board[9]
        return True
    elif board[15] == board[21] == board[27] == board[33] and board[15] != "-":
        winner = board[15]
        return True

    # column 5
    elif board[4] == board[10] == board[16] == board[22] and board[4] != "-":
        winner = board[4]
        return True
    elif board[10] == board[16] == board[22] == board[28] and board[10] != "-":
        winner = board[10]
        return True
    elif board[16] == board[22] == board[28] == board[34] and board[16] != "-":
        winner = board[16]
        return True
    # column 6
    elif board[5] == board[11] == board[17] == board[23] and board[5] != "-":
        winner = board[5]
        return True
    elif board[11] == board[17] == board[23] == board[29] and board[1] != "-":
        winner = board[11]
        return True
    elif board[17] == board[23] == board[29] == board[35] and board[17] != "-":
        winner = board[17]
        return True


def checkDiagonal3x3(board):
    global winner

    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

def checkDiagonal6x6(board):
    global winner

    # diagonal 1
    if board[0] == board[7] == board[14] == board[21] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[8] == board[15] == board[22] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[9] == board[16] == board[23] and board[2] != "-":
        winner = board[2]
        return True
    elif board[3] == board[8] == board[13] == board[18] and board[3] != "-":
        winner = board[3]
        return True
    elif board[4] == board[9] == board[14] == board[19] and board[4] != "-":
        winner = board[4]
        return True
    elif board[5] == board[10] == board[15] == board[20] and board[5] != "-":
        winner = board[5]
        return True
    elif board[6] == board[13] == board[20] == board[27] and board[6] != "-":
        winner = board[6]
        return True
    elif board[7] == board[14] == board[21] == board[28] and board[7] != "-":
        winner = board[7]
        return True
    elif board[8] == board[15] == board[22] == board[30] and board[8] != "-":
        winner = board[8]
        return True
    elif board[9] == board[14] == board[19] == board[24] and board[9] != "-":
        winner = board[9]
        return True
    elif board[10] == board[15] == board[20] == board[25] and board[10] != "-":
        winner = board[10]
        return True
    elif board[11] == board[16] == board[21] == board[26] and board[11] != "-":
        winner = board[11]
        return True
    elif board[12] == board[19] == board[26] == board[33] and board[12] != "-":
        winner = board[12]
        return True
    elif board[13] == board[20] == board[27] == board[34] and board[13] != "-":
        winner = board[13]
        return True
    elif board[14] == board[21] == board[28] == board[35] and board[14] != "-":
        winner = board[14]
        return True
    elif board[15] == board[20] == board[25] == board[30] and board[15] != "-":
        winner = board[15]
        return True
    elif board[16] == board[21] == board[26] == board[31] and board[16] != "-":
        winner = board[16]
        return True
    elif board[17] == board[22] == board[27] == board[32] and board[17] != "-":
        winner = board[17]
        return True

def checkIfWin3x3(board):
    global GameRunning

    if checkHorizontle3x3(board3x3):
        gameBoard3x3(board)
        print(double_sep)
        print(f"Congratulations, the player {winner} WON!")
        print(double_sep)
        GameRunning = False

    elif checkVerticale3x3(board3x3):
        gameBoard3x3(board)
        print(double_sep)
        print(f"Congratulations, the player {winner} WON!")
        print(double_sep)
        GameRunning = False

    elif checkDiagonal3x3(board3x3):
        gameBoard3x3(board)
        print(double_sep)
        print(f"Congratulations, the player {winner} WON!")
        print(double_sep)
        GameRunning = False


def checkIfWin6x6(board):
    global GameRunning
    if checkHorizontle6x6(board):
        gameBoard6x6(board)
        print(double_sep)
        print(f"Congratulations, the player {winner} WON!")
        print(double_sep)
        GameRunning = False

    elif checkVerticale6x6(board):
        gameBoard6x6(board)
        print(double_sep)
        print(f"Congratulations, the player {winner} WON!")
        print(double_sep)
        GameRunning = False

    elif checkDiagonal6x6(board):
        gameBoard6x6(board)
        print(double_sep)
        print(f"Congratulations, the player {winner} WON!")
        print(double_sep)
        GameRunning = False

def checkIfTie3x3(board):
    global GameRunning
    if "-" not in board:
        gameBoard3x3(board)
        print(double_sep)
        print("It is a tie! - nobody won")
        print(double_sep)
        GameRunning = False

def checkIfTie6x6(board):
    global gameRunning
    if "-" not in board:
        gameBoard6x6(board)
        print(double_sep)
        print("It is a tie! - nobody won")
        print(double_sep)
        GameRunning = False

# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def AI3x3(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

def AI6x6(board):
    while currentPlayer == "O":
        position = random.randint(0, 35)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


"""
------------------------------------------------------------------------------------------------------------------------
                                                 LOGIN AND GAME SELECT
------------------------------------------------------------------------------------------------------------------------
                                                                                                                    """
# user login/register
print("Welcome in our game center.", "For play you need to be registered so that we can save your stat.", sep="\n")
while True:
    print("Are you registered? ---> select 'login'  |  Else 'register' please:")
    inf = input(">>> ")
    if inf.lower() == "login":
        print(double_sep)

        username = input("Enter your username: ")
        if username not in login_data.keys():
            print("Incorrect username!   Returning to action select...", sep, sep="\n")
            continue

        while True:
            password = input("Enter your password: ")
            if password != login_data[username]:
                print("Incorrect password!", "", sep="\n")

            else:
                break
        print("", "Login successful", "Continuing to app...", "", sep="\n")
        break

    elif inf.lower() == "register":
        print(double_sep)
        while True:
            username = input("Enter your username: ")

            if username in login_data.keys():
                print("A user with this username already exist!", "", sep="\n")
                continue
            else:
                break

        password = input("Enter your password: ")

        login_data[username] = password
        print("", "Thanks for registration", "Continuing to app...", sep,"", sep="\n")
        break
    else:
        print("Unknown option", "", sep="\n")

print(game.center(58), sep, sep="\n")
"""
------------------------------------------------------------------------------------------------------------------------
                                                 Bulls & Cows
------------------------------------------------------------------------------------------------------------------------                    
"""

while True:
    print("Please select game what you want to play:")
    select = input("Game >>> ")
    print(sep, "", sep="\n")

    if select.lower() == "Bulls&Cows".lower():
        print(f"Hi {username}", sep,  "I've generated a random 4 digit number for you.",
              "Let's play a bulls and cows game.", sep, sep="\n")
        start = time.time()     # time counter

        while bulls < 4:
            bulls = 0
            cows = 0
            player_num = input("Enter a 4 digits number: ")
            print(code)

            if len(player_num) < 4 or len(player_num) > 4:      # check if the number has 4 digits
                print("The number must have 4 digits!", sep, sep="\n")
                continue
            elif not player_num.isnumeric():        # check if the number is numeric
                print("Invalid number", sep, sep="\n")
                continue
            elif "0" in player_num[0]:      # check that the number doesn't start with a zero 
                print("number must not start with 0", sep, sep="\n")
                continue

            for dupl in set(player_num):
                result = player_num.count(dupl)
                if result > 1:
                    print("Cannot contain duplicate numbers!", sep, sep="\n")
                    break
                continue
            else:
                attempt += 1
                num_l = list(player_num)
                p = list(map(int, num_l))

                for a in range(len(code)):
                    if p[a] in code and p[a] != code[a]:
                        cows += 1
                    elif p[a] in code and p[a] == p[a]:
                        bulls += 1

                print(f">>> {player_num}")
                if cows <= 1 and bulls <= 1:
                    print(f"{bulls} bull, {cows} cow", sep, sep="\n")
                elif cows > 1 and bulls > 1:
                    print(f"{bulls} bulls, {cows} cows", sep, sep="\n")
                elif cows <= 1 and bulls > 1:
                    print(f"{bulls} bulls, {cows} cow", sep, sep="\n")
                elif cows > 1 and bulls <= 1:
                    print(f"{bulls} bull, {cows} cows", sep, sep="\n")

        if attempt <= 5:
            end = time.time()
            print(f"Correct, you've guessed the right number in {attempt} guesses and {round(end-start, 2)}s!", "That's amazing", sep, sep="\n")
        elif attempt <= 10:
            end = time.time()
            print(f"Correct, you've guessed the right number in {attempt} guesses and {round(end-start, 2)}s!", "That's average", sep, sep="\n")
        elif attempt > 10:
            end = time.time()
            print(f"Correct, you've guessed the right number in {attempt} guesses and {round(end-start, 2)}s!", "That's not so good", sep,
                  sep="\n")


        again = input("Do you want play again? [YES/NO]:")

        if again.lower() == "yes":
            print("We return you to game selection...")
            print("", game.center(58), sep, sep="\n")
            bulls = 0
            start = 0
            end = 0
            code = random.sample(range(1, 9), 4)
            continue
        
        else:
            print("""
        Thank you for playing this game!
        Shutting down...
        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ """)
            quit()

        """
        ----------------------------------------------------------------------------------------------------------------
                                                     Tic-tac-toe
        ----------------------------------------------------------------------------------------------------------------               
        """

    elif select.lower() == "Tic-tac-toe".lower():
        print(f"{username} welcome to Tic Tac Toe!", double_sep, sep="\n")
        tictactoe = True

        while tictactoe:
            game_board = input("Select game board: | 3x3 | 6x6 | >>> ")

            if game_board == "3x3":
                print("")
                print("""GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
    * horizontal,
    * vertical or
    * diagonal row""")
                print(double_sep, "", sep="\n")

                while GameRunning:
                    gameBoard3x3(board3x3)
                    pInput3x3(board3x3)
                    checkIfWin3x3(board3x3)
                    checkIfTie3x3(board3x3)
                    switchPlayer()
                    AI3x3(board3x3)
                    checkIfWin3x3(board3x3)
                    checkIfTie3x3(board3x3)

                again = input("Do you want play again? [YES/NO]: ")

                if again.lower() == "yes":
                    print(f"Do you want play again this game [1] or different [2]?")
                    again = input(">>>")
                    if again == "1":
                        print(sep)
                        currentPlayer = "X"
                        winner = None
                        GameRunning = True
                        board3x3 = board1
                        continue

                    elif again == "2":
                        tictactoe = False
                        currentPlayer = "X"
                        winner = None
                        GameRunning = True
                        board3x3 = board1
                        print("", game.center(58), sep, sep="\n")

                    else:
                        print("", "Unknown operation", "Terminating the application", double_sep, "", "", sep="\n")
                        quit()
                else:
                    print("""
           Thank you for playing this game!
           Shutting down...
           ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯""")
                    quit()


            elif game_board == "6x6":
                print("")
                print("""GAME RULES:
Each player can place one mark (or stone)
per turn on the 6x6 grid. The WINNER is
who succeeds in placing four of their
marks in a:
    * horizontal,
    * vertical or
    * diagonal row""")
                print(double_sep)

                while GameRunning:
                    gameBoard6x6(board6x6)
                    pInput6x6(board6x6)
                    checkIfWin6x6(board6x6)
                    checkIfTie6x6(board6x6)
                    switchPlayer()
                    AI6x6(board6x6)
                    checkIfWin6x6(board6x6)
                    checkIfTie6x6(board6x6)

                again = input("Do you want play again? [YES/NO]:")

                if again.lower() == "yes":
                    print(f"Do you want play again this game [1] or different [2]?")
                    again = input(">>>")
                    if again == "1":
                        print(sep)
                        currentPlayer = "X"
                        winner = None
                        GameRunning = True
                        board6x6 = board2
                        continue

                    elif again == "2":
                        currentPlayer = "X"
                        winner = None
                        GameRunning = True
                        tictactoe = False
                        board6x6 = board2
                        print("", game.center(58), sep, sep="\n")
                    else:
                        print("", "Unknown operation", "Terminating the application", double_sep, "", "", sep="\n")
                        quit()
                else:
                    print("""
            Thank you for playing this game!
            Shutting down...
            ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯""")
                    quit()


        else:
                print("Unknown game board!", "", sep="\n")


    else:
        print("Unknown game 😒", sep, sep="\n")
        continue