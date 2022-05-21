# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: MemoryGame.py
# ==========================
import time
from os import path
import random
import Util

Game_name = path.basename(__file__)  # get THIS file's name. Help to differentiate in game's logs.


# ==========================
# Function: play
#   Purpose: Will call the functions and play the game
#   Return: True/False if the user won/lost.
# ==========================
def play(difficulty_level):
    Util.my_log("(%s) difficulty level: %s" % (Game_name, difficulty_level))
    print("\n*** Welcome to %s! (difficulty level: %s) ***" % (Game_name.strip(".py"), difficulty_level))

    # according to difficulty level, find the corresponding range boundaries
    range_min, range_max = guessing_range(difficulty_level)
    generated_list = generate_sequence(range_max)
    display_hide_list(generated_list, difficulty_level)

    players_list = get_list_from_user()
    player_win = is_list_equal(generated_list, players_list)
    print("My list is: %s" % generated_list)
    return player_win


# ==========================
# Function: guessing_range
#   Purpose: calc range boundaries (min, max)
#   Return: range_min, range_max.
#   Logic:
#       for level n, list length is n
#       examples: for difficulty=1, list length 1 / for difficulty=5, list length 5
# ==========================
def guessing_range(difficulty_level):
    range_min = 1
    range_max = 1 * difficulty_level
    return range_min, range_max


# ==========================
# Function: generate_sequence
#   Purpose: generate a list of random numbers between 1 and 101.
#       The list length will be <difficulty> (1..5).
#   Return: the generated list
# ==========================
def generate_sequence(range_max):
    generated_list = []
    for i in range(range_max):
        generated_list.append(random.randint(1, 100))
    Util.my_log("(%s) Generated list of numbers: %s" % (Game_name, generated_list))
    return generated_list


# ==========================
# Function: display_hide_list
#   Purpose: display the generated list for <0.7 * difficult level> seconds (0.7..3.5)
#   Return: None
# ==========================
def display_hide_list(generated_list, difficulty_level):
    total_numbers = len(generated_list)
    total_chars = len(str(generated_list))
    print("This is my list. Remember it!\nYou'll have %.1f seconds for this..." % (0.7*difficulty_level))
    input("Press any key when ready...")
    print("%s" % generated_list, end="")
    time.sleep(0.7 * difficulty_level)
    # deletes the generated list & prints ? instead (for hiding effect)
    print("\r" * total_chars, "? " * total_numbers)


# ==========================
# Function: get_list_from_user
#   Purpose: return a list of numbers prompted from the user.
#       The list length will be in the size of 'difficulty'
#   Return:
# ==========================
def get_list_from_user():
    players_list = (input("What was my list? > ")).split()
    players_list = [int(s) for s in players_list if s != " "]
    Util.my_log("Player's list: %s" % players_list)
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
