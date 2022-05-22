# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: Utils.py
# Purpose:
#   A general purpose python file.
#   This file will contain general information and operations we need for the game
# ==========================

from os.path import join
from os import system, name
from time import strftime


time_format = "%Y%m%d_%H%M%S"
timestamp = strftime(time_format)

PATH_TO_LOG_FILE = "c:\\temp\\wog"
LOG_FILE_NAME = "wog_%s.log" % timestamp
LOG_FILE = join(PATH_TO_LOG_FILE, LOG_FILE_NAME)

SCORES_FILE_NAME = 'wog_scores.txt'
BAD_RETURN_CODE = -999


def write_to_file(data):
    with open(LOG_FILE, "a") as file:
        file.write(data)


def my_log(msg, msg_type="log", stdout="file", action="cont"):
    # msg_type:
    #   "log" - general logs (default)
    #   "info" - for benchmarks
    #   "err" - for error alerts
    #   "debug" - for debug purposes
    time_format_d = "%Y-%m-%d %H:%M:%S"
    timestamp_d = strftime(time_format_d)
    msg_type = msg_type.upper()
    if stdout == "file":
        write_to_file(("\n[%s][%s] %s" % (msg_type, timestamp_d, msg)))
    else:
        print(("[%s][%s] %s" % (msg_type, timestamp_d, msg)))

    # action:
    #   "cont" - continue the normal execution (default)
    #   "stop" - stops the program execution
    if action == "cont":
        return
    elif action == "stop":
        quit(0)
    else:  # wrong input for arg 'action'! report error & continue to run
        if stdout == "file":
            write_to_file("\n[err][%s] Wrong arg for my_log action!" % timestamp)
        else:
            print("\n[err][%s] Wrong arg for my_log action!" % timestamp)


# clear the console
def screen_cleaner():
    system('cls' if name == 'nt' else 'clear')


# print the welcome msg for each game module & report to log file
def welcome_to_game(game_name, difficulty_level):
    my_log("(%s) difficulty level: %s" % (game_name, difficulty_level))
    screen_cleaner()
    print("\n\n*** Welcome to %s! ***" % game_name.strip(".py"))
    print("\ndifficulty level: %s" % difficulty_level)
