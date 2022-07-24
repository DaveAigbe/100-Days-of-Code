from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}  # Store the current card after it is produced by the "next_card" function


# ---------------------------- CARD FLIP ------------------------------#

def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text=data.columns[1])
    canvas.itemconfig(card_word, text=current_card["English"])


# ---------------------------- NEXT CARD ------------------------------- #

data = pandas.read_csv('data/french_words.csv')  # Convert the csv file into a pandas dataframe that can be worked with

# Create a dictionary out of the words in the format of {{'French': fword, 'English':eword}, {'French': fword2, 'English':eword2}, etc...}
to_learn = data.to_dict(orient='records')

filename = 'known_words.txt'


def next_card():
    global current_card

    # Each time the card is a new card is shown, change its title and color
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text=data.columns[0])

    # Grab a random dictionary from inside the dictionary that holds a pair of the French word + its translations
    current_card = random.choice(to_learn)

    # First try to grab the data out of the text file holding the known words
    try:
        with open(filename, 'r') as f:
            known_words = f.read().split()
    except FileNotFoundError:  # If it's the users first time entering the program, create file instead
        with open(filename, 'w') as file:
            file.write('')
    else:
        # In the case that the word is not in the data of known words, display it on the card and after 3 seconds flip to show the translation
        if current_card["French"] not in known_words:
            canvas.itemconfig(card_word, text=current_card["French"])
            window.after(3000, flip_card)
        # If the card is in the data list, then run the function again to attempt to obtain a different word.
        else:
            next_card()


# ---------------------------- KNOWN OR UNKNOWN BUTTONS ------------------------------- #

def correct_translation():
    global current_card

    # Obtain the word from the global variable and store it as the next line in the text file
    with open(filename, 'a') as f:
        f.write(f'{current_card["French"]}\n')

    # After the
    next_card()


def wrong_translation():
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

# -- Create Window
window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# -- Create Canvas
canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(450, 300, image=card_front_image)
card_title = canvas.create_text(450, 150, text='title', font=("Arial", 40, "italic"))
card_word = canvas.create_text(450, 290, text='word', font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, sticky='EW')

# -- Create Buttons
wrong_button_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_button_image, bg=BACKGROUND_COLOR, bd=0, command=wrong_translation)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file='images/right.png')
right__button = Button(image=right_button_image, bg=BACKGROUND_COLOR, bd=0, command=correct_translation)
right__button.grid(column=1, row=1)

# After everything is created, to start off the program call the next card
next_card()

# -- Keep window open
window.mainloop()
