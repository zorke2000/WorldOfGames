# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: MainGame.py
# ==========================

from Live import welcome, load_game

player = input("What's your name? ")
print(welcome(player))
load_game()
