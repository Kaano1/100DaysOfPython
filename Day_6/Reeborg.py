#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#We solved Maze.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
while at_goal() != True:
    if right_is_clear():
        turn_right()
    if front_is_clear():
        move()
    elif not front_is_clear():
        turn_left()