import json

with open("Menu_CoffeeMachine.json") as file:
    info_coffee = json.load(file)

resources = {
    "water" : 500,
    "coffee" : 50,
    "milk" : 500
}

def payment(coffee_price):
    coins = {
        "quarter": 0.25,
        "dime": 0.10,
        "nickel": 0.05,
        "penny": 0.01
    }

    sum_coins = 0

    for coin, value in coins.items():
        while True:
            try:
                count = int(input(f"How many {coin}s? "))
                if count < 0:
                    print("Please enter a non-negative integer. Try again.")
                    continue
                sum_coins += count * value
                print(f"Total so far: ${sum_coins:.2f}")
            except ValueError:
                print("Type an integer. Try again.")

            if sum_coins >= coffee_price:
                change = sum_coins - coffee_price
                print(f"Here's your change: ${change:.2f}.")
                print("Your coffee. Enjoy!")
                return

    else:
        print(f"Sorry, you don't have enough money. Please take your money: {sum_coins:.2f}.")


def checking_resources(coffee_choice):
        coffee_data = info_coffee[coffee_choice]
        if (resources["water"] >= coffee_data["water"] and
            resources["coffee"] >= coffee_data["coffee"] and
            resources["milk"] >= coffee_data["milk"]):

            resources["water"] = resources["water"] - coffee_data["water"]
            resources["coffee"] = resources["coffee"] - coffee_data["coffee"]
            resources['milk'] = resources["milk"] - coffee_data["milk"]

            print(f"${coffee_data['price']}. Insert coins please.")
            payment(coffee_data['price'])
        else:
            print("We don't have sufficient resources. Ending the program.")
            return

def choosing_coffee():
    while True:
        try:
            coffee = int(input("Which coffee do you want to drink? Type menu number: "))
            if coffee in [1,2,3]:
                checking_resources(coffee - 1)
                break
            else:
                print("Incorrect menu. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        choosing_coffee()


if __name__ == "__main__":
    print("COFFEE MACHINE")
    print("""MENU:
    1. Cappuccino - $3.00
    2. Latte - $2.50
    3. Espresso - $1.50""")
    main()
