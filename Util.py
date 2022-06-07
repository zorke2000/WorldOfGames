# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: Utils.py
# Purpose:
#   A general purpose python file.
#   This file will contain general information and operations we need for the game
# ==========================

from os import system, name, path, mkdir
from time import strftime

time_format = "%Y%m%d_%H%M%S"
timestamp = strftime(time_format)

SESSION_ENDED = True
LOG_DIR = "logs"
LOG_FILE_NAME = "wog_%s.log" % timestamp
LOG_FILE = path.join(LOG_DIR, LOG_FILE_NAME)

FILES_DIR = "files"
SCORES_FILE_NAME = 'wog_scores.txt'
SCORES_FILE = path.join(FILES_DIR, SCORES_FILE_NAME)
BAD_RETURN_CODE = -1

text_attr = {
    'bold': '\033[1m',
    'red': '\033[91m',
    'blue': '\033[94m',
    'end': '\033[0m'
}


def init_folders():
    try:
        mkdir(LOG_DIR)
    except OSError:
        pass
        # print("Something went wrong with creating the '%s' folder or it's already exist.." % LOG_DIR)

    try:
        mkdir(FILES_DIR)
    except OSError:
        pass
        # print("Something went wrong with creating the '%s' folder or it's already exist.." % FILES_DIR)


def write_to_log_file(info):
    with open(LOG_FILE, "a") as file:
        file.write(info)


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
        write_to_log_file(("\n[%s][%s] %s" % (msg_type, timestamp_d, msg)))
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
            write_to_log_file("\n[err][%s] Wrong arg for my_log action! (code: %s)" % (timestamp, BAD_RETURN_CODE))
        else:
            print("\n[err][%s] Wrong arg for my_log action! (code: %s)" % (timestamp, BAD_RETURN_CODE))


# clear the console
def screen_cleaner():
    system('cls' if name == 'nt' else 'clear')


# print the welcome msg for each game module & report to log file
def welcome_to_game(game_name, difficulty_level):
    my_log("(%s) difficulty level: %s" % (game_name, difficulty_level))
    screen_cleaner()
    print("\n\n*** Welcome to %s%s%s! ***" % (text_attr['blue'], game_name.strip(".py"), text_attr['end']))
    print("\nDifficulty level: %s%s%s" % (text_attr['red'], difficulty_level, text_attr['end']))
