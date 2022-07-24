def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
        if front_is_clear():
            move()
        else:
            turn_left()
    elif not wall_in_front() and wall_on_right() and front_is_clear():
        move()
        if wall_on_right():
            turn_left()
            if wall_in_front():
                turn_right()
            else:
                move()
        if right_is_clear():
            turn_right()
            while front_is_clear():
                move()
    elif wall_in_front() and not wall_on_right():
            turn_right()
            while front_is_clear():
                move()
    elif not wall_in_front() and not wall_on_right():
        move()



  #https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json