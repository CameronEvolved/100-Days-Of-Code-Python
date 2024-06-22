# Project Name: Escaping the Maze
# Source: Day 6 project from 100 days of code course
# What does it do: Allows robot to solve any maze from Reeborg's World
# Note: This code was specifically created to be used for the puzzle linked below
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


#allows the robot to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() == False:
    think(0)
    #Check if facing a wall
    if wall_in_front() == True:
        #check if right is clear, turn and move 1 space
        if right_is_clear() == True:
            turn_right()
            move()
        else:
            turn_left()    
    #move forward if not facing a wall
    else:
        if right_is_clear() == True:
            if is_facing_north == True:
                move()
            turn_right()
            move()
        else:
            move()


#Note that there is a bug in this my code that causes a loop under a very specific starting situation (see loop screenshot).
#This happened in the instructors version of the code as well and she said learn how to fix it around day 15.