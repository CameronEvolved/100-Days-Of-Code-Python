# Project Name: Treasure Island
# Source: Day 3 project from 100 days of code course
# What does it do?: It's a choose your own adventure type of game, based on the choices provided from the challenge.

print('''
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
     ''')

print("Welcome to treasure island! Your mission is to find the treasure. Let's begin....")
print("You've arrived on the island and you can go left or right. Which do you choose?")
direction = input('Type "left" or "right" ')
#changing the users input to all lowercase to avoid crash
direction = direction.lower()

if direction == "left":
    print("A wise choice.")
else:
    print("You have fallen into a hole and died.")
    print("Game Over.")
    exit()

print("After walking for some time, you start to feel hot. You could swim to cool off, ")
print("or you could stay on the island and wait under a tree. Which to you choose?")
move = input('Type "swim" or "wait ')
#changing the users input to all lowercase to avoid crash
move = move.lower()

if move == "wait":
    print("A wise choice.")
else:
    print("The water was filled with hungry fish. You were attacked by a trout and died.")
    print("Game Over.")
    exit()

print("While waiting by the tree, you see an opening to a cave, so you go there.")
print("In the cave, you see 3 doors and a sign with a fairy on it that says ")
print("'You should not be here, but now you must continue. It's too late to turn back now.'")
print("'1 door leads to treasure, all others lead to certain death. Choose wisely.'")
print("Which door will you choose? ")
door = input('Type "red", blue, yellow, or wait')
#changing the users input to all lowercase to avoid crash
door = door.lower()

if door == "yellow":
    print("You find a room full of treasure and safe passage off of the island")
    print("You Win!.")
    exit()

elif door == "red":
    print("You are set on fire and you burned to death.")
    print("Game Over.")
    exit()

elif door == "blue":
    print("You enter a dark room, and are eating alive by beasts.")
    print("Game Over.")
    exit()

else:
    print("Feeling overwhelmed, you start to panic and die of a heart attack.")
    print("Game Over.")
    exit()





