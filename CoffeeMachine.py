import json

print("COFFEE MACHINE")
print("""MENU:
1. Cappuccino - $3.00
2. Latte - $2.50
3. Espresso - $1.50""")

with open("Menu_CoffeeMachine.json") as file:
    info_coffee = json.load(file)

coins = {"penny" : 0.01,
         "dime" : 0.10,
         "nickel" : 0.05,
         "quarter" : 0.25}
resources = {
    "water" : 500,
    "coffee" : 50,
    "milk" : 500
}

def payment():
    pass

def checking_resources(coffee):
        if coffee == 1:
            coffee = 0
        elif coffee == 2:
            coffee = 1
        else:
            coffee = 2

        if info_coffee[coffee]["water"] >= resources["water"] and info_coffee[coffee]["coffee"] >= resources["coffee"] and \
                info_coffee[coffee]["milk"] >= resources["milk"]:
            print(f"${info_coffee[coffee]['price']} please.")
        else:
            print("We don't have sufficient resources. Try choose another coffee.")

def choosing_coffee():
    while True:
        coffee = input("Which coffee do you want to drink? Type menu number: ")
        if coffee != 1 or coffee != 2 or coffee != 3:
            print("Incorrect menu. Try again.")
            continue
        else:
            checking_resources(coffee)
