import random

from Hangman_Art import logo as logo, stages as stages
from Hangman_Words import word_list as word_list


lives = 5
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = list("-" * word_length )

game_won = False

print(logo,"\n")

used_letters = []
while not game_won:
    if '-' not in display:
        print(f"Complete word: {chosen_word}")
        print('You win!')
        game_won = True
        break

    guess = str(input("Guess a letter: ")).lower().strip()
    print('\n'*80)
    while guess in used_letters:
        print(f"You've already guessed {guess}")
        print(''.join(display))
        guess = str(input("Guess a letter: ")).lower().strip()

    if guess not in used_letters:
        used_letters.append(guess)

    for index in range(word_length):
        if guess == chosen_word[index]:
            display[index] = guess
            print(''.join(display))

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            print("You lose.")
            print(stages[0])
            print(f"The correct word was {chosen_word}")
            break
        print(''.join(display))
        print(stages[lives])
        lives -= 1