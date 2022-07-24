import pandas
import time as t

# TODO 1. Create a dictionary in this format:

filename = 'nato_phonetic_alphabet.csv'
alphabet_data = pandas.read_csv(filename)

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
letters = False
while not letters:
    word = list(input('Enter a word: ').upper())

    try:
        nato_translation = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        t.sleep(1)
        print('Translating word...')
        t.sleep(1)
        print('Formatting translation...')
        t.sleep(1)
        print(nato_translation)
        letters = True
