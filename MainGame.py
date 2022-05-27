# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: MainGame.py
# ==========================

import Live
from Util import screen_cleaner, SESSION_ENDED
from Score import reset_score_file


screen_cleaner()
reset_score_file()
# total_games = 0
player = input("What's your name? ")
Live.welcome(players_name=player)

while True:
    end_session = Live.load_game()
    if end_session == SESSION_ENDED:
        quit(0)
    # total_games += 1
    input("\nPress any key when ready...")
    screen_cleaner()
