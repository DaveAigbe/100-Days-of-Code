from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager():
    def __init__(self):
        self.all_cars = []

    def add_car(self):
        chance = randint(0, 6)
        if chance == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.setheading(180)
            car.penup()
            car.move_increment = 10
            car.color(choice(COLORS))
            car.goto(300, randint(-250, 250))
            self.all_cars.append(car)

    def drive(self):
        for car in self.all_cars:
            if car.xcor() > 280:
                new_x = car.xcor() - STARTING_MOVE_DISTANCE
                car.goto(new_x, car.ycor())
            else:
                new_x = car.xcor() - car.move_increment
                car.goto(new_x, car.ycor())

    def reset_and_move(self):
        for car in self.all_cars:
            car.goto(randint(350, 900), randint(-230, 230))

    def increase_speed(self):
        for car in self.all_cars:
            car.move_increment += 3

# class CarManager(Turtle):  # Alternate code using inheritance
#     def __init__(self):
#         super().__init__()
#         self.shape('square')
#         self.shapesize(stretch_len=2, stretch_wid=1)
#         self.setheading(180)
#         self.penup()
#         self.move_increment = 10
#         self.color(choice(COLORS))
#         self.goto(randint(310, 900), randint(-230, 230))
#
#     def drive(self):
#         if self.xcor() > 280:
#             new_x = self.xcor() - STARTING_MOVE_DISTANCE
#             self.goto(new_x, self.ycor())
#         else:
#             new_x = self.xcor() - self.move_increment
#             self.goto(new_x, self.ycor())
#
#     def reset_and_move(self):
#         self.goto(randint(350, 900), randint(-230, 230))
#
#     def increase_speed(self):
#         self.move_increment += 3
