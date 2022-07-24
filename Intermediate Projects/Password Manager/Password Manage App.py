from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = 'Helvetica'


# ---------------------------- SEARCH PASSWORDS ------------------------------- #
def search_information():
    website = website_entry.get().title()
    filename = 'data.json'
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title='Database Empty', message=f'Password database is empty, please try adding a password before searching.', icon='error')
    else:
        try:
            # Look for data corresponding to the website in the dictionary, format it, then store it as a request variable
            request = f"Email: {data[website]['username']}\n\nPassword: {data[website]['password']}"
        except KeyError as error_value:
            # If website is not found in dictionary, prompt user to try to enter a different website
            messagebox.showerror(title='Website Not Found', message=f'Website "{error_value}" was not found, please try again.', icon='error')
        else:
            # If website is found in dictionary, show a popup dialog of the previously formatted request variable
            messagebox.showinfo(website, request, icon='info')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def populate_password():
    # Create randomized password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # List comprehension to create all the values inside the random m password
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = ''.join(password_list)

    # After password is shuffled and brought together copy it to the clipboard, so it can be used immediately
    pyperclip.copy(password)

    # Add password to the password entry field
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_information():
    # Store all the user entered informationw
    website = website_entry.get().title()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {"username": username, "password": password}}

    # Format the info into one organized line
    formatted_info = f'{website} | {username} | {password}\n'

    # If the website name or the password is left blank, send out an error message
    if not website and not password:
        messagebox.showerror(title='Entries Missing', message='Please enter a valid website name and password.')
    elif not website:
        messagebox.showerror(title='Entry Missing', message='Please enter a valid website name.')
    elif not password:
        messagebox.showerror(title='Entry Missing', message='Please enter a valid website password.')
    else:
        # If all fields have been filled out, then the information is valid and user will be prompted to save
        answer = messagebox.askokcancel(message=f'Details Entered:\n\n{formatted_info}\nWould you like to save?',
                                        icon='question', title=website)
        if answer:  # If the user clicks on ok, save the data and clean it out, otherwise do nothing

            # Create/Add to a data folder that will hold all password information
            filename = "data.json"
            try:
                # If the json file already exists, this means an entry/entries have already been stored
                # Must open in read mode to use the update function so that the json file adds to the dictionary, rather than replacing it
                with open(filename, 'r') as f:
                    # Read old data
                    data = json.load(f)
                    # Update old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                # If json file does not exits, this means no entries have been added yet, create new json file and inform user
                messagebox.showinfo(title='New Database', message='Generating new database for information.', icon='info')
                with open(filename, 'w') as f:
                    json.dump(new_data, f, indent=4)
            else:
                # Dictionary has been updated at this point, so now replace the old dictionary with the new one
                with open(filename, 'w') as f:
                    # Save updated data as new data
                    json.dump(data, f, indent=4)
            finally:
                # After datas has been stored, clear out all the entry boxes, and reset the position of the cursor to the first entry
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

# -- Create Window
window = Tk()
window.title('Password Manager')
window.config(bg='white', pady=50, padx=50)

# -- Create Canvas
canvas = Canvas(bg='white', height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# -- Create Labels
website_label = Label(text='Website:', bg='white', font=(FONT_NAME, 10, "bold"))
website_label.grid(column=0, row=1, sticky='W')

username_label = Label(text='Email/Username:', bg='white', font=(FONT_NAME, 10, "bold"))
username_label.grid(column=0, row=2, sticky='W')

password_label = Label(text='Password:', bg='white', font=(FONT_NAME, 10, "bold"))
password_label.grid(column=0, row=3, sticky='W')

# -- Create Label Boxes
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, sticky='EW', pady=5)

username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky='EW', pady=5)
username_entry.insert(0, 'dave.aigbe@outlook.com')

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky='EW', pady=5)

# -- Create Buttons
generate_button = Button(text='Generate Password', highlightthickness=0, bg='gray', font=(FONT_NAME, 10, "bold"),
                         command=populate_password)  # ^
generate_button.grid(column=2, row=3, sticky='EW', pady=2)

add_button = Button(text='Add', width=36, highlightthickness=0, bg='gray', font=(FONT_NAME, 10, "bold"),
                    command=save_information)  # ^
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')

search_button = Button(text='Search', highlightthickness=0, bg='#529ad1', font=(FONT_NAME, 10, "bold"),
                       command=search_information)  # ^
search_button.grid(column=2, row=1, sticky='EW', pady=5)
# -- Keep window open
window.mainloop()
