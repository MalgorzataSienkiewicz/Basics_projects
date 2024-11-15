import random

bids = {}

items = ["Mona Lisa image", "Phone Nokia 3310", "Pokemon card with Pikachu"]


def welcome():
    print("Welcome to the secret auction program.")
    name = input("What is your name? ")
    auction_item = random.choice(items)
    print(f"Hello {name}! Today you can buy {auction_item}.")
    return name, auction_item

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
                break
        else:
            while True:
                decision = input("Would you like to place a higher offer? Type 'yes', or press enter and finish submitting offers. ").lower()
                if decision == "yes":
                    break
                elif decision == "":
                    return bid
                else:
                    print("Incorrect command. Try again.")
def start_game():
    name, auction_item = welcome()
    bid = offer()
    bids[name] = bid
    return bids, auction_item

def find_highest_bidder(bidding_dictionary):
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
    return f"The winner is {winner} with a bid of ${bidding_dictionary[winner]}."
def main():
    while items:
        bids, auction_item = start_game()
        while True:
            should_continue = input(f"Are there any other bidders? Type 'yes', or press enter and conclude the auction {auction_item}.").lower()
            if should_continue == 'yes':
                print("\n" * 100)

            elif should_continue == "":
                print(bids)
                print(find_highest_bidder(bids))
                print("Press Enter to exit the auction.")
                break
            else:
                print("Incorrect command. Try again.")
                continue

        items.remove(auction_item)
        if items:
            print("It's time for the next auction.")
        else:
            print("Thank you, everyone. We don't have any items to auction. Goodbye!")
            break
main()









