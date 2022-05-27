# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: MainGame.py
# ==========================

import Live
from Util import screen_cleaner

screen_cleaner()
player = input("What's your name? ")
Live.welcome(players_name=player)

total_games = 0
wins = 0
while True:
    player_win = Live.load_game()
    if player_win == -1:
        if total_games != 0:
            print("\nYour score: %s/100 (%s wins in %s games)"
                  % (int(wins / total_games * 100), wins, total_games))
        print("\nThank you & goodbye!")
        quit(0)
    elif player_win:
        wins += 1
        print("\nGreat! You win!")
    else:
        print("\nNo luck this time...")

    total_games += 1
    input("\nPress any key when ready...")
    screen_cleaner()
