from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.speed('fastest')
        self.setheading(90)
        self.x = x
        self.y = y
        self.goto(self.x, self.y)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(self.x, self.y)
