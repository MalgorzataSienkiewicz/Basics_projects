import random

bids = {}
items = ["Mona Lisa image", "Phone Nokia 3310", "Pokemon card with Pikachu"]
def draw():
    if len(items) > 0:
        auction_item = random.choice(items)
        items.remove(auction_item)
        return auction_item
    return None

def welcome(auction_item):
    print("Welcome to the secret auction program.")
    name = input("What is your name? ").strip()
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
        break
    return bid

def find_highest_bidder(bidding_dictionary):
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
    return f"The winner is {winner} with a bid of ${bidding_dictionary[winner]}."
def main():
    end_auction = False
    auction_item = draw()

    while True:
        name = welcome(auction_item)
        bid = offer()
        bids[name] = bid

        while True:
            should_continue = input(f"Are there any other bidders? Type 'yes', or press enter and conclude the auction {auction_item}. ").lower()
            if should_continue == 'yes':
                print("\n" * 100)
                break
            else:
                print(bids)
                print(find_highest_bidder(bids))
                decision = input("Do yo want to continue the auction with another item? Type 'yes', or press enter to exit the auction. ")
                if decision == "yes":
                    auction_item = draw()
                    if auction_item:
                        print("It's time for the next auction.")
                        bids.clear()
                        break
                    else:
                        print("Thank you, everyone. We don't have any items to auction. Goodbye!")
                        end_auction = True
                        break
                else:
                    print("Thank you, everyone. Goodbye!")
                    end_auction = True
                    break
        if end_auction == True:
            break


main()









