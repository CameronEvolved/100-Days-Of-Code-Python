# Project Name: Hangman
# Source: Day 7 project from 100 days of code course
# What does it do: You choose a letter and try to guess the correct word. You get 5 incorrect guesses.

import random
import hangman_art
import hangman_words

#pulls random word from handman_words module
chosen_word = random.choice(hangman_words.word_list)

word_length = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#create blanks
display = []
for _ in range(word_length):
    display += "_"
    
#get input from user and forces as lowercase
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    #checks letter against each letter (and position) in the word
    for position in range(word_length):
        letter = chosen_word[position]
        #replaces bank slow with the correct letter
        if letter == guess:
            display[position] = letter

    #checks is user is wrong
    if guess not in chosen_word:
        print(f"\"{guess}\" is not one of the words")
        #reduces life for each wrong answer
        lives -= 1
        #checks if user has any lives left and ends of live = 0
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #checks is the user has guessed all of the letters correctly.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #this prints the ascii art from the handman_words module
    print(hangman_art.stages[lives])