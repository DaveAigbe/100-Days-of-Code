from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 60, 'bold')


class UserBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # score that will be altered as snake eats food
        self.penup()  # do not show pentrail of scoreboard
        self.goto(100, 200)
        self.hideturtle()  # hide the turtle, so it does not show up on the screen
        self.color('white')  # color the scoreboard white because the default setting is black and the screen is black
        self.user_board()  # create the board when the game starts

    def user_board(self):
        self.write(arg=f'{self.score}', move=False, align=ALIGNMENT, font=FONT)  # write the score out

    def increase_score(self):  # method to increase the score as the user eats food
        self.score += 1  # add 1 to the score attribute
        self.clear()  # clear out the screen so the scores do not overlap
        self.user_board()  # create new board with updated score


