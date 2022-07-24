from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 23, 'normal')
filename = 'data.txt'
with open(filename) as f:
    current_high = f.read()



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # score that will be altered as snake eats food
        self.high_score = int(current_high)
        self.penup()  # do not show pentrail of scoreboard
        self.sety(265)  # set the position of the scoreboard
        self.hideturtle()  # hide the turtle, so it does not show up on the screen
        self.color('white')  # color the scoreboard white because the default setting is black and the screen is black
        self.create_board()  # create the board when the game starts

    def create_board(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)  # write the score out

    def game_over(self):
        self.goto(0, 0)  # game over message will be in the middle of the screen
        self.write(arg='GAME OVER', align=ALIGNMENT,font=FONT)

    def increase_score(self): # method to increase the score as the user eats food
        self.score += 1  # add 1 to the score attribute
        self.create_board()  # create new board with updated score

    def reset(self):
        if self.score > int(current_high):
            self.high_score = self.score
            with open(filename, 'w') as f:
                f.write(str(self.score))
        self.score = 0
        self.create_board()