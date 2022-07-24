from random import randint
from game_data import data
from art import logo, vs

used_index = []


def find_unused_index():
    run_again = True
    while run_again:
        number = randint(0, len(data) - 1)
        if number in used_index:
            pass
        else:
            used_index.append(number)
            return int(number)


def game():
    print(logo)
    person1 = find_unused_index()
    game_score = 0

    for turns in range(0, len(data) - 1):
        person2 = find_unused_index()

        if game_score > 0:
            print(f"You're right! Current score: {game_score}")
        print(f"Compare A: {data[person1]['name']}, a {data[person1]['description']}, from {data[person1]['country']}.")
        print(vs)
        print(f"Versus B: {data[person2]['name']}, a {data[person2]['description']}, from {data[person2]['country']}.")

        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        print("\n")

        if user_answer == 'a':
            if data[person1]["follower_count"] > data[person2]["follower_count"]:
                person1 = person2
                game_score += 1
            else:
                print(f"Sorry that's wrong. Final score: {game_score}")
                break
        elif user_answer == 'b':
            if data[person2]["follower_count"] > data[person1]["follower_count"]:
                person1 = person2
                game_score += 1
            else:
                print(f"Sorry that's wrong. Final score: {game_score}")
                break


def user_input():
    play_or_not = input("Would you like to play a game of Higher Lower? (Y/N) ").lower()

    if play_or_not == 'y':
        return True
    else:
        return False



