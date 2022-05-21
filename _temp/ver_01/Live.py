# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: MainGame.py
# ==========================

# get & verify correct user input
def get_players_input(input_list):
    while True:
        user_input = input(" %s > " % input_list)
        if int(user_input) not in input_list:
            print("Wrong input! Please try again...")
            continue
        else:
            break
    return True


def welcome(name):
    # name must be of type string...
    if type(name) != str:
        name = str(name)

    msg = "Hello " + name + " and welcome to the World of Games (WoG)!"
    msg += "\nHere you can find many cool games to play."
    return msg


def load_game():
    # Player should choose the game...
    msg = 'Please choose a game to play:'
    msg += '\n 1. Memory Game - a sequence of numbers will appear for 1 second' \
           ' and you have to guess it back'
    msg += '\n 2. Guess Game - guess a number and see if you chose like the computer'
    msg += '\n 3. Currency Roulette - try and guess the value of a random amount' \
           ' of USD in ILS'
    print(msg)
    get_players_input([1, 2, 3])

    # Player should choose game's level of difficulty
    print("Please choose game difficulty from 1 to 5 (1-beginner, 5-Master).")
    get_players_input([1, 2, 3, 4, 5])
