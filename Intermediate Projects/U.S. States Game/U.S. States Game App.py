import pandas
import turtle

data = pandas.read_csv('50_states.csv')
state_names = data.state.tolist() # Extract all the states into a list

screen = turtle.Screen()
screen.setup(width=726, height=492)
screen.title('U.S. States Game')
image = 'blank_states_img.gif'  # Image of the U.S.
screen.addshape(image)  # Add it to the shape list that turtle can use (turtle,square,arrow etc..)
turtle.shape(image)  # Create a turtle that uses the image

writing = turtle.Turtle()  # Create a new instance of turtle, this one will be used for writing
used_states = []
states_to_learn = []
correct = 0


def writing_states(): # Function that determines if/where turtle will write
    if answer.title() in state_names:  # If the user answer(not case-sensitive) is in the list of states
        writing.hideturtle()
        writing.penup()
        writing.goto(int(data[data.state == answer.title()].x), int(data[data.state == answer.title()].y)) # Extract x and y coordinates from specific state
        writing.write(answer.title())  # When coordinates have been reached, write onto screen the state name
        return True  # The return true or false help with scoring system as well as ignoring duplicates
    else:
        return False


while correct != 50:  # While user has not guessed all 50, continue prompting
    answer = screen.textinput(title=f'{correct}/50 States Correct', prompt="What's a state name?")
    if answer == 'exit':  # If exit is typed, a csv file generating all of the states that were missed will be created
        states_to_learn = [state for state in state_names if state.lower() not in used_states]
        practice_states = pandas.DataFrame(states_to_learn)
        practice_states.to_csv(f'states_to_learn_{50-correct}')
        break
    else:
        if writing_states():
            if answer not in used_states:
                used_states.append(answer)
                correct += 1

turtle.mainloop()
