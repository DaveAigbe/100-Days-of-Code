from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # starting positions of three segment snake
MOVE_DISTANCE = 20  # snake will move 20 pixels each time
# Angles that will be used to determine what user key presses do
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []  # hold all the segments (Starting and New) for the snake
        self.screen = Screen()
        self.create_snake()
        self.create_screen()
        self.head = self.segments[0]  # the head of the snake is the first segment in the list "segments"

    def create_screen(self): # setting up screen
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Snake Game')
        self.screen.tracer(0) # turns off the animation for the turtle, so it will move smoothly
        self.screen.listen()  # screen will react to key presses

    def create_snake(self): # method to create the initial snake
        for position in STARTING_POSITIONS: # for each coordinate in the STARTING_POSITIONS list, add a segment
            self.add_segment(position)

    def add_segment(self, position): # method to create a single segment of the snake
        segment = Turtle()
        segment.penup()
        segment.shape('square')
        segment.color('green')
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):  # when snake eats food, add a segment to the end of the snake
        self.add_segment(self.segments[-1].position())

    def move_forward(self):  # Next 4 methods deal with what snake will do when user presses specific key
        if self.head.heading() == LEFT:
            self.head.right(90)
        elif self.head.heading() == UP or self.head.heading() == DOWN:
            pass
        else:
            self.head.left(90)

    def move_downward(self):
        if self.head.heading() == LEFT:
            self.head.left(90)
        elif self.head.heading() == DOWN or self.head.heading() == UP:
            pass
        else:
            self.head.right(90)

    def turn_left(self):
        if self.head.heading() == DOWN:
            self.head.right(90)
        elif self.head.heading() == LEFT or self.head.heading() == RIGHT:
            pass
        else:
            self.head.left(90)

    def turn_right(self):
        if self.head.heading() == DOWN:
            self.head.left(90)
        elif self.head.heading() == RIGHT or self.head.heading() == LEFT:
            pass
        else:
            self.head.right(90)

    def move(self):  # method to deal with how snake will move and key press setup

        self.screen.update()  # update the screen each time a new segment moves

        for position_num in range(len(self.segments) - 1, 0, -1): # starting from the back of the snake
            new_x = self.segments[position_num - 1].xcor()  # the x value of segment in front of the current segment becomes the current segments x value
            new_y = self.segments[position_num - 1].ycor()  # same as above, except using y coordinate
            self.segments[position_num].goto(new_x, new_y)  # the current segment will now be moved up essentialy one position

        self.head.forward(MOVE_DISTANCE)  # snake will move forward by 20 pixels
        # actives key presses for user, deciding what key has what function
        self.screen.onkey(fun=self.move_forward, key='Up')
        self.screen.onkey(fun=self.move_downward, key='Down')
        self.screen.onkey(fun=self.turn_left, key='Left')
        self.screen.onkey(fun=self.turn_right, key='Right')

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def screen_close(self):
        self.screen.exitonclick()
