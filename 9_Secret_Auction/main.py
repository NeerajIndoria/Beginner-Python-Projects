import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids={}
want_to_bid = True
while want_to_bid:
    name = input("What is your name? : ")
    bid_price = int(input("What\'s your bid : $"))
    bids[name] = bid_price
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if choice == 'no':
        want_to_bid = False
        find_highest_bidder(bids)
    elif choice == 'yes':
        os.system('cls')
