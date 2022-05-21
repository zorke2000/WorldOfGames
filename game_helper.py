# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: game_helper.py
# Purpose: useful multi-purpose functions
# ==========================

from os.path import join
from time import strftime


time_format = "%Y%m%d_%H%M%S"
timestamp = strftime(time_format)
debug_file = join("files", ("debug_%s" % timestamp))


def write_to_file(data):
    with open(debug_file, "a") as file:
        file.write(data)


def debug(msg, msg_type="log", stdout="file", action="cont"):
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
            write_to_file("\n[err][%s] Wrong arg for debug action!" % timestamp)
        else:
            print("\n[err][%s] Wrong arg for debug action!" % timestamp)
