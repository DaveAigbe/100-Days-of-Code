import time
from screen import GameScreen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard


# Create screen
game_screen = GameScreen()

# Create scoreboard
scoreboard = Scoreboard()

# Create player
player = Player()

# Create cars
car_manager = CarManager()


# Check for user key presses
game_screen.user_move(player.go_up)

# Run game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    game_screen.screen_update()
    car_manager.add_car()
    car_manager.drive()

    if player.ycor() > FINISH_LINE_Y:  # If player crossed finish line, reset turtle position and increase score/level and difficulty
        player.new_game()
        scoreboard.increase_level()
        car_manager.reset_and_move()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 23:  # If player collides with a car, game will end
            scoreboard.game_over()
            game_is_on = False

game_screen.screen_exit()
