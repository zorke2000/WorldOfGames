# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: GuessGame.py
# ==========================
# Properties:
#   1. Difficulty
#   2. Secret_number
# Methods:
#   1. generate_number - Will generate number between 1 to difficulty and save it to secret_number.
#   2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and return the number.
#   3. compare_results - Will compare the secret generated number to the one prompted by the get_guess_from_user.
#   4. play - Will call the functions above and play the game. Will return True / False if the user lost or won.
# ==========================

from os import path
import game_helper
import random

Game_name = path.basename(__file__)  # get THIS file's name. Help to differentiate in game's logs.


# ==========================
# Function:
#   Purpose: calc range boundaries (min, max)
#   Return: range_min, max_range.
#   Logic:
#       level 1: 4 digits numbers (1,000..9,999)
#       level 5: 8 digits numbers (10,000,000..99,999,9999)
#       example: for difficulty=1, min is 10^3 & max is (10^4 - 1)
# ==========================
def guessing_range(difficulty_level):
    range_min = 10**(difficulty_level+2)
    max_range = 10**(difficulty_level+3)-1
    return range_min, max_range


# ==========================
# Function:
#   Purpose: to call the other functions & play the game.
#   Return: True/False if the user won/lost.
# ==========================
def play(difficulty_level):
    game_helper.debug("(%s) difficult level: %s" % (Game_name, difficulty_level))
    secret_number = generate_number(difficulty_level)
    users_guess = get_guess_from_user()


# ==========================
# Function:
#   Purpose: to generate number between 1 to 'difficulty' and save it to 'secret_number'.
#   Return: 'secret_number'
# ==========================
def generate_number(difficulty_level):
    range_min = guessing_range(difficulty_level)[0]
    max_range = guessing_range(difficulty_level)[1]

    secret_number = random.randint(range_min, max_range)
    game_helper.debug("(%s) secret number= %d | min=%d, max=%d" % (Game_name, secret_number, range_min, max_range))
    return secret_number


# ==========================
# Function:
#   Purpose: to prompt the user for a number between 1 to 'difficulty' and return the number.
#   Return: user's guess
# ==========================
def get_guess_from_user():
    pass


# ==========================
# Function:
#   Purpose: to compare the secret generated number to the one prompted by the get_guess_from_user.
#   Return: True/False if numbers are matched or not.
# ==========================
def compare_results():
    pass
