# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: MainGame.py
# ==========================

import Live


player = input("What's your name? ")
Live.welcome(players_name=player)

total_games = 0
wins = 0
while True:
    player_win = Live.load_game()
    total_games += 1
    if player_win == -1:
        print("\nYour score: %s/100 (%s wins in %s games)"
              % (int(wins/total_games*100), wins, total_games))
        print("\nThank you & goodbye!")
        quit(0)
    elif player_win:
        wins += 1
        print("You win! Kudos! ")
    else:
        print("Well... you may succeed next time :)")
