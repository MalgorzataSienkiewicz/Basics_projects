
def menu():
    print('Welcome w menu!')

    print("1. Wyświetl użytkowników.")
    print("2. Dodaj użytkownika.")
    print("3. Usuń użytkownika")
    print("4. Wyjdź z programu.")

def loop():
    while True:
            menu()
            choice = input('Który punkt z menu Cie interesuje? ').strip()

            if not choice.isdigit():
                print("Musisz podać cyfre od 1 do 4.")
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
                print("W menu są tylko punkty od 1 do 4.")
def choice_one():
         with open("Uzytkownicy z programu - menu.txt", "r") as file:
            users = file.readlines()
            print("Oto lista użytkowników:")
            for user in users:
                print(user.strip())
def choice_two():

         with open("Uzytkownicy z programu - menu.txt", "r") as file:
            users = file.readlines()
            new_user = input("Wpisz imie użytkownika, którego chcesz dodać: ").strip()
            if new_user + '\n' in users:
                print("Użytkownik o takiej nazwie już istnieje.")
            else:
                with open("Uzytkownicy z programu - menu.txt", 'a') as file:
                    file.write(new_user + '\n')
                    print(f'Dodano użytkownika {new_user}!')
                    users.append(new_user)
                    print("Oto lista użytkowników:")
                    for user in users:
                        print(user.strip())
def choice_three():

        with open("Uzytkownicy z programu - menu.txt", "r") as file:
            users = file.readlines()
            print("Oto lista użytkowników:")
            for user in users:
                print(user.strip())
                remove_user = input("Wpisz imię użytkownika, którego chcesz usunąć: ").strip()
                if remove_user + '\n' in users:
                    users.remove(remove_user + '\n')
                    with open('Uzytkownicy z programu - menu.txt', 'w') as file:
                        file.writelines(users)
                    print(f'Usunięto użytkownika {remove_user}!')
                    print("Oto lista użytkowników:")
                    for user in users:
                        print(user.strip())

                else:
                    print("Użytkownika o takiej nazwie nie ma w menu.")
                    user_list =(input("Jeżeli chcesz wyświetlić listę użytkówników wpisz 'tak' "))
                    print("Oto lista użytkowników:")
                    if user_list == 'tak':
                        for user in users:
                            print(user.strip())

loop()








