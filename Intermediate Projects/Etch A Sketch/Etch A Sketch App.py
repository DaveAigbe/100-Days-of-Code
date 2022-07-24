from turtle import Turtle, Screen

sketch = Turtle()
sketch.color('purple2')

screen = Screen()
screen.colormode(255)
screen.listen()


def move_forward():
    sketch.forward(10)


def move_backward():
    sketch.backward(10)


def turn_left():
    sketch.tilt(10)
    tilt = sketch.tiltangle()
    sketch.setheading(tilt)


def turn_right():
    sketch.tilt(-10)
    tilt = sketch.tiltangle()
    sketch.setheading(tilt)


def clear():
    sketch.clear()
    sketch.penup()
    sketch.home()
    sketch.pendown()


screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=clear, key='c')

screen.exitonclick()
