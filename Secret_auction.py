import random

bids = {}

items = ["Mona Lisa image", "Phone Nokia 3310", "Pokemon card with Pikachu"]
auction_item = random.choice(items)

def welcome():
    print("Welcome to the secret auction program.")
    name = input("What is your name? ")
    print(f"Hello {name}! Today you can buy {auction_item}.")
    return name

def offer():
    while True:
        try:
            bid = int(input("What is your offer? Enter only integer:$  "))
        except ValueError:
            print("Your bid isn't integer. Try again.")
            continue
        print(f"Your offer: {bid}")
        for key, value in bids.items():
            if bid <= value:
                print("Your offer must be higher than the current offer. ")
        decision = input("Would you like to type a higher offer? Type 'yes' or finish your game.").lower()
        if decision == "yes":
            continue
        else:
            return bid

def start_game():
    name = welcome()
    bid = offer()
    bids[name] = bid
    return bids

def find_highest_bidder(bidding_dictionary):
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
    return f"The winner is {winner} with a bid of ${bidding_dictionary[winner]}."

while True:
    start_game()
    should_continue = input("Are there any other bidders? Type 'yes' or finish your game.").lower()
    if should_continue == 'yes':
        print("\n" * 100)
        continue
    else:
        print(bids)
        print(find_highest_bidder(bids))




