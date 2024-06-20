# Project Name: Tip Calculator
# Source: Day 2 project from 100 days of code course
# What does it do: Generates the total bill w/tip included. Also splits bill based on the number of people.

print("Welcome to the tip calculator!")
bill = input("What is the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
#converting the tip into a percent number
tip_percent = int(tip) / 100
#percent of the bill in tips
bill_percent_with_tip = float(tip_percent) * float(bill)
#add tip to the original bill
total_bill = float(bill_percent_with_tip) + float(bill)
#total bill and divide by the number of people who will split
final_amount = float(total_bill) / int(people)

print(f"Each person should pay: ${round(final_amount, 2)}")