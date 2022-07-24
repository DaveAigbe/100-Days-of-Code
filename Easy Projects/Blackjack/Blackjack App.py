from art import logo as logo
from bj_functions import start_game as start_game, playing_blackjack as playing_blackjack

if start_game():  # if user says they want to start game, if not exit
    print(logo)
    playing_blackjack()
else:
    exit()






