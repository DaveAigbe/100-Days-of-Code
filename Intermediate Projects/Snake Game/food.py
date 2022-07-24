from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # setup shape of food
        self.penup()  # when the food moves, no pen trail
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # make the food hitbox smaller
        self.color('brown')
        self.speed('fastest')  # when the food moves positions, do not show its movement
        self.move_food()  # move the first bit of food as the game begins

    def move_food(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)  # food moves to random position inside of the screen area
