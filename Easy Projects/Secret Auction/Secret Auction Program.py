from art import greet_user as greet_user
from finding_winner import highest_bidder as higher_bidder

names_with_bid = {}
bidders = True

greet_user()

while bidders:
    name = input("What is your name?: ").title()
    bid = int(input("What is your bid?: $"))
    names_with_bid[name] = bid
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bids == 'yes':
        print("\n"*30)
        continue
    else:
        bidders = False

higher_bidder(names_with_bid)