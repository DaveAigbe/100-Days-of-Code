import random
from art import logo as logo


def game_outcome(user, computer):  # Function that will check for winners that have hit 21, or are over 21
    if sum(user) == sum(computer) and sum(user) == 21:  # if both the computer and user have hit 21, it's a draw.
        present_final(user, computer)
        print("Draw 🙃")
        return True
    elif sum(user) == 21: # if the user has hit 21, you win.
        present_final(user, computer)
        print("User win with a Blackjack 😎")
        return True
    elif sum(computer) == 21: # if the computer has hit 21, they win.
        present_final(user, computer)
        print("Computer win with a Blackjack 😎")
        return True
    elif sum(user) > 21:  # if the user went over 21, you lose.
        present_final(user, computer)
        print("You went over. You lose 😭")
        return True
    elif sum(computer) > 21:  # if the computer went over 21, they lose.
        present_final(user, computer)
        print("Opponent went over. You win 😁")
        return True
    else:  # If none of these options are executed, return False, letting the program know no one has hit or went over 21
        return False


def under_21_outcome(user, computer):  # Function that will check game results if both computer and user ended up with less than 21
    computer_check = 21 - sum(computer)  # Checks how far each player is from 21
    user_check = 21 - sum(user)
    if computer_check == user_check:  # If they are equal length, it is a draw
        print("Draw 🤕")
    elif computer_check < user_check:  # if computer is closer, they win.
        print("You lose 😤")
    else:  # if computer is not closer, you win.
        print("You win 😁")


def start_game():  # Function that will start the game
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play == 'y':  # If user entered 'y' for play, the function will return True, causing the game to start
        return True
    else:  # Otherwise, the function will return False, causing the program to exit
        return False


def draw_card():  # Function that gives the user the option to add a card to their deck or not
    draw_again = input("Type 'y' to get another card, type 'n' to pass: ")

    if draw_again == 'y':  # If the user entered 'y' for draw, the function will return True, causing a card to be added to their deck
        return True
    else:  # Otherwise, the function will return False, causing the game to look for the winner
        return False


def define_ace(user, computer, card_list):  # This function configures how the ace will work inside of a players deck because it can either be valued as 11 or 1
    if card_list[0] in user and sum(user) > 21 and card_list[0] in computer and sum(computer) > 21:  # If both decks contain an ace card AND they are over 21, the ace card will be valued at 1
        user[user.index(card_list[0])] = 1  # This line finds where the ace card is inside of the players list and swaps that index
        computer[computer.index(card_list[0])] = 1
        return user, computer
    elif card_list[0] in user and sum(user) > 21:  # If the users deck contains an ace card and is over 21, the ace card will now be valued at 1
        user[user.index(card_list[0])] = 1
        return user, computer
    elif card_list[0] in computer and sum(computer) > 21: # If the computers deck contains an ace card and is over 21, the ace card will now be valued at 1
        computer[computer.index(card_list[0])] = 1
        return user, computer
    else:  # If the ace card is in the deck but it does not cause the player to go over 21, leave it as 11, or if the ace is not in their deck, do nothing
        return False


def present_current(user, computer):  # Presents game stats as game goes on
    print(f'Your cards: {user}, current score: {sum(user)}')
    print(f"Computer's first card: {computer[0]} \n")


def present_final(user, computer): # Presents game has ended
    print(f'Your final hand: {user}, final: {sum(user)}')
    print(f"Computer's final hand: {computer}, final: {sum(computer)} \n")


def user_option(user, computer, card_list):
    print('\n')  # For formatting, makes output easier to read
    if draw_card():  # If user chose to draw a card
        user.append(random.choice(card_list))  # Add a card to their deck
        define_ace(user, computer, card_list)  # Check to see if there is an ace and whether or not it causes score to break 21
        if sum(computer) < 17:  # As long as the computers score is under 17, whether the player chooses to hold or draw, the computer will draw
            computer.append(random.choice(card_list))
            define_ace(user, computer, card_list)
        if sum(user) > 21: # If the user chose to draw and this caused them to break 21, find the outcome of the game
            game_outcome(user, computer)
            pass
        else:  # If they chose to draw and did not break 21, present the score, and ask them if they want to draw another card
            present_current(user, computer)
            user_option(user, computer, card_list)
    else:  # If user chose to hold
        if sum(computer) < 17:  # If the computer is under total is under 17, while user chose to hold, the computer will draw
            computer.append(random.choice(card_list))
            define_ace(user, computer, card_list)  # Checks to see if there is an ace and configures it to best fit the deck
        if game_outcome(user, computer): # Check to see if there is a draw, a player broke 21, or if a player hit 21
            pass
        else:  # Otherwise, present the final score and full list of each user, then find out who is closer to 21 or if they are tied
            present_final(user, computer)
            under_21_outcome(user, computer)


def playing_blackjack():  # Function dictates how the game is run
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # All the choices of cards available

    user_cards = [random.choice(cards) for _ in range(2)]  # Each new game both players start with 2 random cards
    computer_cards = [random.choice(cards) for _ in range(2)]
    define_ace(user_cards, computer_cards, cards)  # If player has ace configure it to best suit their deck
    # The line above is important because a player could recieve [11,11] which would cause them to automatically lose, define_ace would change that to [1,11]
    present_current(user_cards, computer_cards)  # Present your inital deck and the computers first number
    if game_outcome(user_cards, computer_cards):  # If someone won off their first deck, one such as [11,10], then the game is over
        if not start_game():  # If user chooses not to start game
            exit()  # if user says they are done playing after computer/user won off first round
        else:  # If they choose to start another game
            print('\n')  # For formatting, makes output easier to read
            while start_game():  # While start game is true (set to 'y'), it will keep running the game after each winner is found
                print(logo)
                print("\n" * 20)  # To clear out console
                playing_blackjack()  # When the game is over it will go back to start game, asking the user if they want to play again
            else:  # If they choose not to play again, while loop will break and it will end up here where program exits
                exit()
    else:  # If no player won off of the first round
        user_option(user_cards, computer_cards, cards)  # Ask the user whether they would like to draw again or not
        print('\n')  # For formatting, makes output easier to read
        while start_game():  # Keep the game running as long as user enters 'y'
            print(logo)
            print("\n" * 20)
            playing_blackjack()
        else:
            exit()
