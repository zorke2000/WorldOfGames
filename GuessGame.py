# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: GuessGame.py
# ==========================

from os import path
import Util
import random

Game_name = path.basename(__file__)  # get THIS file's name. Help to differentiate in game's logs.


# ==========================
# Function: play
#   Purpose: to call the other functions & play the game.
#   Return: True/False if the user won/lost.
# ==========================
def play(difficulty_level):
    Util.my_log("(%s) difficulty level: %s" % (Game_name, difficulty_level))
    print("\n*** Welcome to %s! (difficulty level: %s) ***" % (Game_name.strip(".py"), difficulty_level))

    # according to difficulty level, find the corresponding range boundaries
    range_min, range_max = guessing_range(difficulty_level)
    secret_number = generate_number(range_min, range_max)
    players_guess = get_guess_from_user(range_min, range_max)

    player_win = compare_results(secret_number, players_guess)
    print("My number is: %s" % secret_number)
    return player_win


# ==========================
# Function: guessing_range
#   Purpose: calc range boundaries (min, max)
#   Return: range_min, range_max.
#   Logic:
#       for level n, the numbers' range is 1..5n
#       examples: for difficulty=1, range 1..5 / for difficulty=5, range 1..25
# ==========================
def guessing_range(difficulty_level):
    range_min = 1
    range_max = 5 * difficulty_level
    return range_min, range_max


# ==========================
# Function: generate_number
#   Purpose: to generate number between 1 to 'difficulty' and save it to 'secret_number'.
#   Return: 'secret_number'
# ==========================
def generate_number(range_min, range_max):
    secret_number = random.randint(range_min, range_max)
    Util.my_log("(%s) secret number= %d | min=%d, max=%d" % (Game_name, secret_number, range_min, range_max))
    return secret_number


# ==========================
# Function: get_guess_from_user
#   Purpose: to prompt the user for a number between 1 to 'difficulty' and return the number.
#   Return: user's guess
# ==========================
def get_guess_from_user(range_min, range_max):
    players_guess = input("Guess my number! It's between %d-%d  > " % (range_min, range_max))
    return int(players_guess)


# ==========================
# Function: compare_results
#   Purpose: to compare the secret generated number to the one prompted by the get_guess_from_user.
#   Return: True/False if numbers are matched or not.
# ==========================
def compare_results(secret_number, players_guess):
    if secret_number == players_guess:
        return True
    else:
        return False
