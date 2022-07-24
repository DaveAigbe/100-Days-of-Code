file_letters = './Input/Letters/starting_letter.txt'
file_names = './Input/Names/invited_names.txt'


with open(file_letters) as f:
    letter = f.readlines()

with open(file_names) as f:
    names = f.read()
    names = names.split() # separates each name into


greetings = []

for pos in range(len(names)):
    file_output = f'./Output/ReadyToSend/letter_for_{names[pos]}.txt' # name will change for each individual
    if pos == 0:
        greetings.append(letter[0].replace('[name]', names[pos])) # first name replaces the template
    else:
        greetings.append(letter[0].replace(names[pos-1], names[pos]))  # replace, the previous name with current one
    letter[0] = greetings[pos]  # set the old greeting to the new one
    with open(file_output, 'w') as f:
        f.write(''.join(letter))  # create a new letter and store it in ReadyToSend

    
