# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: MainGame.py
# ==========================

# import os
import Util
import CurrencyRouletteGame
import GuessGame
import MemoryGame


games_list = {
    0: "Quit",
    1: "Memory game",
    2: "Guess game",
    3: "Currency roulette"
}

difficulty_levels = {
    1: "Beginner",
    2: "Graduate",
    3: "Advance",
    4: "Expert",
    5: "Master"
}


# ==========================
# Function:
#   Purpose: get & verify correct user input
#   Return: player's input
# ==========================
def get_players_input(input_list):
    while True:
        players_input = input(" %s > " % input_list)
        # verify input is a DIGIT in the ALLOWED LIST!
        if (not players_input.isdigit()) or (int(players_input) not in input_list):
            print("Wrong input! Please try again...")
            continue
        else:
            break
    return int(players_input)  # must be an int!


# ==========================
# Function:
#   Purpose: Display the Welcome message with player's name
#   Return: None
# ==========================
def welcome(players_name):
    # name must be of type string...
    if type(players_name) != str:
        players_name = str(players_name)

    Util.my_log("Session started...")
    Util.my_log("User name: %s" % players_name, "info")
    print("\nHello %s, welcome to the World of Games!"
          "\nHere you'll find few cool games to play :)" % players_name)


# ==========================
# Function:
#   Purpose: Display the Main menu
#   Return: game_id & difficulty level
# ==========================
def main_menu():
    # Player should choose the game...
    msg = '\n\nPlease choose a game to play:' \
          '\n 0. Quit' \
          '\n 1. Memory Game - a sequence of numbers will appear for 1sec. You have to guess it back.' \
          '\n 2. Guess Game - guess a number and see if you chose like the computer' \
          '\n 3. Currency Roulette - try to guess a value of a random amount of USD in ILS'
    print(msg)
    players_input = get_players_input(list(games_list.keys()))
    if players_input == 0:
        return 0, 0

    Util.my_log("Game selected: %s" % games_list[players_input])
    game_id = players_input

    # Player should choose game's level of difficulty
    print("\nNow, let's choose DIFFICULTY level (1 is beginner, 5 is master):")
    players_input = get_players_input(list(difficulty_levels.keys()))
    Util.my_log("Difficulty level selected: %s" % difficulty_levels[players_input])
    difficulty_level = players_input

    return game_id, difficulty_level


# ==========================
# Function:
#   Purpose: Run the chosen game with the selected difficulty level.
#   Return: True/False whether user win or not. -1 if players wants to quit
# ==========================
def load_game():
    # display the main menu of the games
    game_id, difficulty_level = main_menu()

    if game_id == 0:
        player_win = -1
    elif game_id == 1:
        player_win = MemoryGame.play(difficulty_level)
    elif game_id == 2:
        player_win = GuessGame.play(difficulty_level)
    elif game_id == 3:
        player_win = CurrencyRouletteGame.play(difficulty_level)
    else:
        print("Something went wrong! Got unexpected game number from the input...")
        quit(Util.BAD_RETURN_CODE)

    return player_win
