from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

game_on = True  # Boolean value that keeps game running

while game_on:
    snake.move()  # while the game is still active keep the snake moving
    time.sleep(.1)  # sleep so that the screen update looks fluid

    # Detect collision with food
    if snake.head.distance(food) < 15:  # if the snake head collides with the food within 15 pixels, then add to score, and move the food to a new location
        scoreboard.increase_score()
        snake.extend()
        food.move_food()

    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:  # if snake head hits edge of screen, game over
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:  # if snake head hits any part of body, that is not of course the head, game over
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

snake.screen_close()
