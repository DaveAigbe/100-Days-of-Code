from turtle import Turtle

FONT = ("Elephant", 18, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-245, 260)
        self.hideturtle()
        self.color('black')
        self.display_level()

    def display_level(self):
        self.write(arg=f'Level: {self.level}', move=False, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f'GAME OVER', move=False, align=ALIGNMENT, font=FONT)