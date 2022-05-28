# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: Score.py
# Purpose:
#   A package that is in charge of managing the scores file.
#   The scores file at this point will consist of only a number.
#   That number is the accumulation of the winnings of the user.
#   Amount of points for winning a game is as follows:
#       POINTS_OF_WINNING = DIFFICULTY X 3
#   Each time the user is winning a game, the points he won will be added to his current amount of
#   point saved in a file.
# ==========================
import Util
from Util import my_log, SCORES_FILE
from os import path


# ==========================
# Function: add_score
#   Purpose:
#   Return: none
#   Logic:
#       The function’s input is a variable named difficulty.
#       The function will read the current score in the scores file,
#       and will use it to save the current score.
# ==========================
def add_score(difficulty_level):
    # score before the latest win
    score = read_score_file()
    my_log("Current score: %s" % score, msg_type="info")
    # calc new score after latest win
    new_points = difficulty_level*3
    my_log("For this game, the player scored %s new points." % new_points, msg_type="info")
    score += new_points
    my_log("New score: %s" % score, msg_type="info")
    write_to_score_file(score)


def write_to_score_file(score):
    with open(SCORES_FILE, "w") as file:
        file.write(str(score))


def read_score_file():
    if path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as file:
            return int(file.readline())
    else:
        my_log("Can't read from Score file! (code %s)" % Util.BAD_RETURN_CODE, msg_type="err")
        write_to_score_file(0)
        my_log("Created the Score file. Reset score to 0...", msg_type="info")
        return Util.BAD_RETURN_CODE


def reset_score_file():
    if not path.exists(SCORES_FILE):
        my_log("Score file not exists yet... Create & init it with score 0.", msg_type="info")
    else:
        my_log("Score file already exists. Reset it to score 0.", msg_type="info")
    write_to_score_file(0)
