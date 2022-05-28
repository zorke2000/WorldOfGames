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

import Util

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
    app.run(host='127.0.0.1', port=30000, debug=False)


# accessed via <HOST>:<PORT>/wog_score
@app.route("/wog_score")
def wog_score():
    score = Score.read_score_file()
    if score != Util.BAD_RETURN_CODE:
        return f'<html>' \
               f'<head>' \
               f'<title>Scores Game</title>' \
               f'</head>' \
               f'<body>' \
               f'<h1>Your current score is:' \
               f'<div id="score" style="color:green">{score}' \
               f'</div></h1>' \
               f'</body></html>', 0
    else:
        return f'<html>' \
               f'<head>' \
               f'<title>Scores Game</title>' \
               f'</head>' \
               f'<body>' \
               f'<h1>Your current score is:' \
               f'<div id="score" style="color:red">Cant read the score file! (error code: {score})' \
               f'<div id="score" style="color:red">Resetting the score file...' \
               f'</div></h1>' \
               f'</body></html>', 0
