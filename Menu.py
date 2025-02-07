def menu():
    print('Welcome to the menu!')
    print("1. Display users.")
    print("2. Add user.")
    print("3. Remove user.")
    print("4. Exit the program.")

def choices():
    while True:
        menu()
        choice = input('Which item from the menu interests you? ').strip()

        if not choice.isdigit():
            print("\nEnter a number from the range of 1 to 4.\n")
            continue

        choice = int(choice)

        if choice == 1:
            display_users()
        elif choice == 2:
            add_user()
        elif choice == 3:
            remove_user()
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("The menu only has items from 1 to 4.")

def display_users():
    with open("Users from program - Menu.txt", "a+") as file:
        file.seek(0)  # Move to the start of the file
        content = file.readlines()
        
        if len(content) == 0:
            print("File is empty.")
                
        else:
            print("Here is the list of users:")
            for user in content:
                print(user.strip())
        
        print()
        input("Press enter to continue..")

def add_user():
    while True:
        new_user = input("Which users name would you like to add? ").strip()
        with open("Users from program - Menu.txt", "a+") as file:
            file.seek(0)
            users = file.readlines()

            if new_user + '\n' in users:
                another_name = input("A user with that name already exists. You must choose another username.\n"
                                     "Enter another name or return to menu by entering 1: ")
                if another_name.isdigit() and int(another_name) == 1:
                    break
                else:
                    continue
            else:
                file.write(new_user + '\n')
                print(f'User added: {new_user}!')
                users.append(new_user + '\n')

                print("Here is the updated list of users:")
                for user in users:
                    print(user.strip())

                next_user = input("Do you want to add the next user to the list? \nIf yes enter - 1,\notherwise press enter and return to menu. ")
                if next_user.isdigit() and int(next_user) == 1:
                    continue
                else:
                    break
                

def remove_user():
    with open("Users from program - Menu.txt", "r") as file:
        users = file.readlines()
        
        if not users:
            print("The user list is empty.")
            return
        
        print("Here is the list of users:")
        for user in users:
            print(user.strip())
        
        remove_user = input("Enter the name of the user you want to delete: ").strip()
        if remove_user + '\n' in users:
            users.remove(remove_user + '\n')
            with open('Users from program - Menu.txt', 'w') as file:
                file.writelines(users)
            print(f'User deleted: {remove_user}!')
        else:
            print("There is no user with that name in the list.")


choices()
