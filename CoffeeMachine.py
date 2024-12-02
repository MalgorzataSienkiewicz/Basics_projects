import json

print("COFFEE MACHINE")
print("""MENU:
1. Cappuccino - $3.00
2. Latte - $2.50
3. Espresso - $1.50""")

with open("Menu_CoffeeMachine.json") as file:
    info_coffee = json.load(file)

resources = {
    "water" : 500,
    "coffee" : 50,
    "milk" : 500
}

def payment():
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
                break
            except ValueError:
                print("Type an integer. Try again.")

            print(f"Total so far: ${sum_coins:.2f}")

            if sum_coins > value or sum_coins == value:
                change = sum_coins - value
                print(f"Here's your change: ${change}.")
                print("Your coffee. Enjoy!")
                break
            else:
                print(f"Sorry, you don't have enough money. Please take your money: {sum_coins}.")
                break

def checking_resources(coffee):
        if coffee == 1:
            coffee = 0
        elif coffee == 2:
            coffee = 1
        else:
            coffee = 2

        if info_coffee[coffee]["water"] >= resources["water"] and info_coffee[coffee]["coffee"] >= resources["coffee"] and \
                info_coffee[coffee]["milk"] >= resources["milk"]:
            print(f"${info_coffee[coffee]['price']}. Insert coins please.")
        else:
            print("We don't have sufficient resources. Try choose another coffee.")

def choosing_coffee():
    while True:
        try:
            coffee = int(input("Which coffee do you want to drink? Type menu number: "))
            if coffee == 1 or coffee == 2 or coffee == 3:
                checking_resources(coffee)
                break
            else:
                print("Incorrect menu. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        choosing_coffee()
        payment()

main()
