# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: MainGame.py
# ==========================

import Live
from Util import screen_cleaner, SESSION_ENDED
from Score import reset_score_file
import MainScores

screen_cleaner()
reset_score_file()
player = input("What's your name? ")
Live.welcome(players_name=player)

while True:
    end_session = Live.load_game()
    if end_session == SESSION_ENDED:
        quit(0)
    print("\nTo see your score, go to 127.0.0.1:5000/wog_score\n")
    MainScores.score_server()
    input("\nPress any key when ready...")
    screen_cleaner()
