# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: MainGame.py
# ==========================

import Live
import Util
import Score
import MainScores

Util.screen_cleaner()
Util.init_folders()
Score.reset_score_file()
player_name = input("What's your name? ")
Live.welcome(player_name)

while True:
    end_session = Live.load_game(player_name)
    if end_session == Util.SESSION_ENDED:
        quit(0)
    print("\nTo see your score, go to 127.0.0.1:30000\n")
    MainScores.score_server()
    input("\nPress any key when ready...")
    Util.screen_cleaner()
