import sys

def display_info():
    try:
        with open("shopping_list.txt") as file:
            print(file.read())
    except FileNotFoundError:
        print("The shopping list does not exist yet.\n")
        return

def add_item():
    while True:
            with open("shopping_list.txt", 'a+') as file:
                file.seek(0)
                items = [line.strip() for line in file.readlines()]

                item = input("Type the item which you want to add: ").strip()
                if item in items:
                    print(f"{item} has been added to the list.")
                    print("You have this item on the list.")
                else:
                    file.write(item + "\n")

                break

def remove_item():
    new_shopping_list = []
    try:
        with open("shopping_list.txt") as file:

            for line in file.readlines():
                new_shopping_list.append(line.strip())
            if new_shopping_list == []:
                raise FileNotFoundError

            item = input("Type the item which you want to remove: ")
            if item in new_shopping_list:
                new_shopping_list.remove(item)
                print(f"{item} has been removed to the list.")
            else:
                print(f"{item} is not on the list.")
    except FileNotFoundError:
        print("The shopping list does not exist yet.\n")

    with open("shopping_list.txt", "w") as file:
        for item in new_shopping_list:
            file.write(item + "\n")

while True:
    print("1. Display list.")
    print("2. Add new item.")
    print("3. Remove item.")
    print("4. Exit program.")

    try:
        option = int(input("Type option(1, 2, 3 or 4): ").strip())

        if option == 1:
            display_info()
        elif option == 2:
            add_item()
        elif option == 3:
            remove_item()
        elif option == 4:
            sys.exit()
    except ValueError:
        print("Incorrect option. Type number 1, 2, 3 or 4.")




