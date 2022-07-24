from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(title='Make your bet!', prompt='Who will win the race? Enter a color:')
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']

x_coord = -240
y_coord = -150

all_turtles = []

for turtle_index in range(6):
    racer = Turtle(shape='turtle')
    racer.color(colors[turtle_index])
    racer.penup()
    racer.setposition(x=x_coord,y=y_coord )
    y_coord += 50
    all_turtles.append(racer)

is_race_on = False

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_step = random.randint(0, 10)
        turtle.forward(random_step)
        winning_color = turtle.pencolor()
        if turtle.xcor() > 250:
            if winning_color == bet:
                print(f'You won! The winning color was {winning_color}.')
            else:
                print(f'You lost. The winning color was {winning_color}')
            is_race_on = False

screen.exitonclick()
