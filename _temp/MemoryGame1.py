# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: MemoryGame.py
# ==========================

from os import path
import keyboard
import random
import game_helper

Game_name = path.basename(__file__)  # get THIS file's name. Help to differentiate in game's logs.


# ==========================
# Function: play
#   Purpose: Will call the functions and play the game
#   Return: True/False if the user won/lost.
# ==========================
def play(difficulty_level):
    game_helper.my_log("(%s) difficulty level: %s" % (Game_name, difficulty_level))
    print("\n*** Welcome to %s! (difficulty level: %s) ***" % (Game_name.strip(".py"), difficulty_level))

    # according to difficulty level, find the corresponding range boundaries
    range_min, range_max = guessing_range(difficulty_level)
    generated_list = generate_sequence(range_max)
    print(generated_list)
    display_hide_list(generated_list)

    players_list = get_list_from_user()
    player_win = is_list_equal(generated_list, players_list)
    print("My list is: %s" % generated_list)
    return player_win


# ==========================
# Function: guessing_range
#   Purpose: calc range boundaries (min, max)
#   Return: range_min, range_max.
#   Logic:
#       for level n, list length is 3n
#       examples: for difficulty=1, list length 3 / for difficulty=5, list length 15
# ==========================
def guessing_range(difficulty_level):
    range_min = 1
    range_max = 3 * difficulty_level
    return range_min, range_max


# ==========================
# Function: generate_sequence
#   Purpose: generate a list of random numbers between 1 and 101.
#       The list length will be 'difficulty'.
#   Return:
# ==========================
def generate_sequence(range_max):
    generated_list = []
    for i in range(range_max):
        generated_list.append(random.randint(1, 100))
    game_helper.my_log("(%s) Generated list of numbers: %s" % (Game_name, generated_list))
    return generated_list


# ==========================
# Function: display_hide_list
#   Purpose:
#   Return:
# ==========================
# def display_hide_list(generated_list):
#     total_numbers = len(generated_list)
#     total_chars = len(str(generated_list))
#     print("This is my list. Remember it! When ready click the SPACE bar.")
#     print("%s" % generated_list)
#     keyboard.read_event()  # wait for any KB event
#     # deletes the generated list & prints ? instead (for hiding effect)
#     print("\b" * total_chars, "? " * total_numbers)
def display_hide_list(generated_list):
    total_numbers = len(generated_list)
    total_chars = len(str(generated_list))
    print("This is my list. Remember it!")
    input("When ready click any key. You'll have less than a sec to memorize it...")
    print("%s" % generated_list)
    keyboard.read_event()  # wait for any KB event
    # deletes the generated list & prints ? instead (for hiding effect)
    print("\b" * total_chars, "? " * total_numbers)


# ==========================
# Function: get_list_from_user
#   Purpose: return a list of numbers prompted from the user.
#       The list length will be in the size of 'difficulty'
#   Return:
# ==========================
def get_list_from_user():
    players_list = (input("What was my list? > ")).split()
    players_list = [int(s) for s in players_list if s != " "]
    print("This is the list you entered: %s" % players_list)
    return players_list


# ==========================
# Function: is_list_equal
#   Purpose: To compare two lists if they are equal.
#   Return: True/False if equal or not
# ==========================
def is_list_equal(generated_list, players_list):
    if generated_list == players_list:
        return True
    else:
        return False
