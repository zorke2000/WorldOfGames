# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: MainScore.py
# Purpose:
#   This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with HTML.
#   This is done by using python’s flask library/
# ==========================

import Score
from flask import Flask

app = Flask(__name__)


# ==========================
# Function: score_server
#   Purpose:
#   Return:
#   Logic:
#       This function will serve the score.
#       It will read the score from the scores file and will return an HTML for score or error
# ==========================
def score_server():
    app.run(host='127.0.0.1', port=5000, debug=False)


# accessed via <HOST>:<PORT>/wog_score
@app.route("/wog_score")
def wog_score():
    score = Score.read_score_file()
    return f"Your WOG score: {score}", 0  # status code
