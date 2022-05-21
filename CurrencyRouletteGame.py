# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Project: WorldOfGames (WoG)
# File: CurrencyRouletteGame.py
# ==========================
# This game will use the free currency api to get the current exchange rate from USD to ILS.
# Will generate a new random number between 1-100 & will ask the user to find the value of
# the generated number from USD to ILS.
# Depending on the user’s difficulty his answer will be correct if the guessed value is between
# the interval surrounding the correct answer.
# ==========================
import random
from os import path
import Util
import requests

Game_name = path.basename(__file__)  # get THIS file's name. Help to differentiate in game's logs.
range_min = 1
range_max = 100
currency1 = "USD"
currency2 = "ILS"


# ==========================
# Function:
#   Purpose: Call the functions and play the game.
#   Return: True/False if the user won/lost
# ==========================
def play(difficulty_level):
    Util.my_log("(%s) difficulty level: %s" % (Game_name, difficulty_level))
    print("\n*** Welcome to %s! (difficulty level: %s) ***" % (Game_name.strip(".py"), difficulty_level))

    # generate a random amount in USD to be converted into NIS
    amount_currency1 = random.randint(range_min, range_max)
    Util.my_log("Generated amount (USD): %s" % amount_currency1)

    # check forex API for current currency exchange rate from currency1 to currency2
    conversion_rate = currency_exchange()
    amount_currency2 = calc_currency2_amount(conversion_rate, amount_currency1)
    players_guess = get_guess_from_user(amount_currency1)
    money_interval = get_money_interval(amount_currency2, difficulty_level)
    player_win = check_result(players_guess, money_interval)
    print("The exact amount of %s%s is %s%s. Let's see if you were correct..."
          % (amount_currency1, currency1, amount_currency2, currency2))

    return player_win


# ==========================
# Function: currency_exchange
#   Purpose: using API, find the current exchange rate between currency1 & currency2
#   Return: current conversion rate
# ==========================
def currency_exchange():
    api_key = "37029bdc415426523c2d80c9"

    api_endpoint_pair = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{currency1}/{currency2}'
    api_response = requests.get(api_endpoint_pair)
    conversion_rate = api_response.json()["conversion_rate"]
    Util.my_log("%s-to-%s current conversion rate is: %s" % (currency1, currency2, conversion_rate))
    print("%s-to-%s rate is: ***\n(not going to tell you! this is what's this game is all about..)"
          % (currency1, currency2))

    return conversion_rate

    # TODO: Check to see if USD is a valid currency code
    # print("Something wrong with the currency codes.")
    # game_helper.my_log("currency codes error | code1=%s code2=%s" % (currency1, currency2), msg_type="err")


# ==========================
# Function: get_guess_from_user
#   Purpose: A method to prompt a guess from the user to enter a guess of value to a given amount of USD
#   Return: players guess
# ==========================
def get_guess_from_user(amount_in_usd):
    players_guess = int(input(" > How much is %sUSD in NIS? " % amount_in_usd))
    return players_guess


# ==========================
# Function: get_money_interval
#   Purpose: get the current currency rate from USD to ILS and generates an interval as follows:
#       for given difficulty 'd', and total value of money 't', the interval will be:
#       (t - (5 - d), t + (5 - d))
#   Return: money_interval
# ==========================
def get_money_interval(amount_currency2, difficulty_level):
    accuracy_shoulders_low = amount_currency2 - (5 - difficulty_level)
    accuracy_shoulders_high = amount_currency2 + (5 - difficulty_level)
    money_interval = range(accuracy_shoulders_low, accuracy_shoulders_high + 1)
    Util.my_log("amount currency2= %s , money interval: %s-%s"
                % (amount_currency2, accuracy_shoulders_low, accuracy_shoulders_high))
    return money_interval


# ==========================
# Function:
#   Purpose: check if player's guess is within the allowed money_interval range
#   Return: True/False if player guess is within range or not.
# ==========================
def check_result(players_guess, money_interval, ):
    if players_guess in money_interval:
        players_answer_is_correct = True
    else:
        players_answer_is_correct = False
    return players_answer_is_correct


def calc_currency2_amount(conversion_rate, amount_currency1):
    amount_currency2 = int(amount_currency1 * conversion_rate)
    Util.my_log("Calculated amount (%s): %s" % (currency2, amount_currency2))
    return amount_currency2
