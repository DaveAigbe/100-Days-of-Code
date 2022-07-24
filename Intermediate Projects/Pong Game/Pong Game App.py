from paddle import Paddle
from screen import GameScreen
from ball import Ball
from time import sleep
from computer_board import ComputerBoard
from user_board import UserBoard
from hashed_barrier import HashedBarrier

# Screen Attributes
screen = GameScreen()
user_board = UserBoard()
computer_board = ComputerBoard()
hashed_barrier = HashedBarrier()

# Paddles
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

# Screen button calls
screen.r_paddle_keys(right_paddle.go_up, right_paddle.go_down)
screen.l_paddle_keys(left_paddle.go_up, left_paddle.go_down)

# Ball Attributes
ball = Ball()


game_on = True

while game_on:
    sleep(ball.move_speed) # This will increase each time ball is hit
    screen.screen_update()
    ball.movement()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with r_paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()

    # Detect if ball has passed wall and keep score

    # Detect if right paddle misses
    if ball.xcor() > 380:
        computer_board.increase_score()
        ball.reset_position()
        right_paddle.reset_position()
        left_paddle.reset_position()
    # Detect if left paddle misses
    elif ball.xcor() < -380:
        user_board.increase_score()
        ball.reset_position()
        right_paddle.reset_position()
        left_paddle.reset_position()

screen.screen_exit()

