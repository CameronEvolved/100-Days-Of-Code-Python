# Project Name: Blind Auction
# Source: Day 9 project from 100 days of code course
# What does it do: Bidding system where each entry is entered "blindly" and then the highest entry wins.


# Note I failed this challenge after multiple hours of attempts, 
# I gave up and replaced most of my broken code with the instructors. I'll try to redo this another day.



from replit import clear
from art import logo

#title & logo
print("Blind Auction Simulator")
print(logo)

#dictionary for entries
entries = {}
#variable for when to stop asking for more bids
no_more_bids = False


bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()