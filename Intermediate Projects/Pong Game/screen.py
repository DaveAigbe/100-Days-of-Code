from turtle import Screen


class GameScreen():
    def __init__(self):
        self.g_screen = Screen()
        self.g_screen.bgcolor("black")
        self.g_screen.setup(width=800, height=600)
        self.g_screen.title('Pong Game')
        self.g_screen.listen()
        self.g_screen.tracer(0)

    def screen_exit(self):
        self.g_screen.exitonclick()

    def screen_update(self):
        self.g_screen.update()

    def r_paddle_keys(self, func1, func2):
        self.g_screen.onkeypress(func1, 'Up')
        self.g_screen.onkeypress(func2, 'Down')

    def l_paddle_keys(self, func1, func2):
        self.g_screen.onkeypress(func1, 'w')
        self.g_screen.onkeypress(func2, 's')
