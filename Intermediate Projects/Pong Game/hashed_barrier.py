from turtle import Turtle


class HashedBarrier(Turtle):
    def __init__(self):
        super().__init__()  # hide the turtle, so it does not show up on the screen
        self.color('white')
        self.pensize(5)
        self.shape('square')
        self.penup()
        self.hideturtle()
        self.goto(0, 295)
        self.setheading(270)
        self.speed('fastest')
        self.hashed_line()

    def hashed_line(self):
        self.pendown()
        while self.ycor() > -295:
            self.forward(5)
            self.penup()
            self.forward(15)
            self.pendown()
            self.forward(5)
