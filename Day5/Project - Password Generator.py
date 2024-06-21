# Project Name: Password Generator
# Source: Day 5 project from 100 days of code course
# What does it do: Generates a random password based on your requirements.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
#get user inputs
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#generate list of required letters
gen_letters = random.sample(letters, nr_letters)
#generate list of required numbers
gen_numbers = random.sample(numbers, nr_numbers)
#generate list of required symbols
gen_symbols = random.sample(symbols, nr_symbols)

#combine the 3 results
combined = gen_numbers + gen_letters + gen_symbols

#shuffle results
random.shuffle(combined)

#print results with no spaces
print("Your password is ")
print(*combined, sep='')
