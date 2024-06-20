# Project Name: Rock, Paper, Sissors
# Source: Day 4 project from 100 days of code course
# What does it do: It's a choose your own adventure type of game, based on the choices provided from the challenge.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n" ))

#the game will tell the user which option they chose and show the hand gesture
if user_choice == 0:
    print(f"You chose Rock. \n {rock}")
elif user_choice == 1:
    print(f"You chose Paper. \n {paper}")
elif user_choice == 2:
    print(f"You chose Scissors. \n {scissors}")
#end game early if user does not choose one of the valid options
else:
    print("You have chosen an invalid option. Game over.")
    exit()

#computer will randomly generate a choice
computer_choice = random.randint(0,2)

#the game will tell the user which option they chose and show the hand gesture
if computer_choice == 0:
    print(f"Computer chose Rock. \n {rock}")
elif computer_choice == 1:
    print(f"Computer chose Paper. \n {paper}")
elif computer_choice == 2:
    print(f"Computer chose Scissors. \n {scissors}")

#comparing the two choices (player wins)
#rock vs scissors
if user_choice == 0 and computer_choice == 2:
    print(f"Rock crushes Scissors. You win!")
#paper vs rock
elif user_choice == 1 and computer_choice == 0:
    print(f"Paper covers Rock. You win!")
#scissors vs paper
elif user_choice == 2 and computer_choice == 1:
    print(f"Scissors cuts paper. You win!")

#comparing the two choices (computer wins)
#rock vs scissors
elif computer_choice == 0 and user_choice == 2:
    print(f"Rock crushes Scissors. You lose!")
#paper vs rock
elif computer_choice == 1 and user_choice == 0:
    print(f"Paper covers Rock. You lose!")
#scissors vs paper
elif computer_choice == 2 and user_choice == 1:
    print(f"Scissors cuts paper. You lose!")

else:
    print(f"The game ends in a draw!")