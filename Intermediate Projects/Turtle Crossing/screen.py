from turtle import Screen


class GameScreen:
    def __init__(self):
        self.g_screen = Screen()
        self.g_screen.setup(width=600, height=600)
        self.g_screen.title('Turtle Crossing')
        self.g_screen.listen()
        self.g_screen.tracer(0)

    def screen_exit(self):
        self.g_screen.exitonclick()

    def screen_update(self):
        self.g_screen.update()

    def user_move(self, func):
        self.g_screen.onkeypress(func, 'Up')
