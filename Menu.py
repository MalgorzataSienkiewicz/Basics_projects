
def menu():
    print('Welcome to the menu!')

    print("1. Display users.")
    print("2. Add user.")
    print("3. Remove user.")
    print("4. Exit the program.")

def loop():
    while True:
            menu()
            choice = input('Which item from the menu interests you? ').strip()

            if not choice.isdigit():
                print("Enter a number from the range of 1 to 4.")
                continue

            choice = int(choice)

            if choice == 1:
                choice_one()
            elif choice == 2:
                choice_two()
            elif choice == 3:
                choice_three()
            elif choice == 4:
                break
            else:
                print("The menu only has items from 1 to 4.")
def choice_one():
         with open("Users from program - Menu.txt", "r") as file:
            users = file.readlines()
            print("Here is the list of users:")
            for user in users:
                print(user.strip())
def choice_two():

         with open("Users from program - Menu.txt", "r") as file:
            users = file.readlines()
            new_user = input("Enter the name of the user you want to add:").strip()
            if new_user + '\n' in users:
                print("A user with that name already exists.")
            else:
                with open("Users from program - Menu.txt", 'a') as file:
                    file.write(new_user + '\n')
                    print(f'User added {new_user}!')
                    users.append(new_user)
                    print("Here is the list of users:")
                    for user in users:
                        print(user.strip())
def choice_three():

        with open("Users from program - Menu.txt", "r") as file:
            users = file.readlines()
            print("Here is the list of users:")
            for user in users:
                print(user.strip())
                remove_user = input("Enter the name of the user you want to delete:").strip()
                if remove_user + '\n' in users:
                    users.remove(remove_user + '\n')
                    with open('Users from program - Menu.txt', 'w') as file:
                        file.writelines(users)
                    print(f'User deleted{remove_user}!')
                    print("Here is the list of users:")
                    for user in users:
                        print(user.strip())

                else:
                    print("There is no user with that name in the menu.")
                    user_list =(input("If you want to display the list of users, type 'yes'."))
                    print("Here is the list of users:")
                    if user_list == 'yes':
                        for user in users:
                            print(user.strip())

loop()








