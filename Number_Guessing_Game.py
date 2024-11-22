import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1,100)

def checking(guess,number):
    hint = ""
    result = ""
    if guess > number:
        hint = "To high."
    elif guess < number:
        hint = "To low."
    else:
        result = "win"
    return hint, result

        
def easy_level(number):
    attempts = 10
    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if not isinstance(guess, int):
            print("You must type integer. Try again")
            attempts -= 1
            continue
        else:
           result, hint  = checking(guess,number)
           if result != "win":
               print(f"{hint}. Guess again")
               attempts -= 1
               continue
           else:
               break
    return result


def hard_level(number):
    attempts = 5
    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if not isinstance(guess, int):
            print("You must type integer. Try again")
            attempts -= 1
            continue
        else:
           result, hint = checking(guess,number)
           print(f"{hint}. Guess again.")
           if result != "win":
               attempts -= 1
               continue
           else:
               break
    return result
    

def choose_difficulty(number):
    while True:
        difficulty = input("Type 'easy' or 'hard': ").lower().strip()
        if isinstance(difficulty, str):
            if difficulty == "easy":
                easy_level(number)
            elif difficulty == "hard":
                hard_level(number)
            else:
                print("Incorrect command. Try again.")
                continue
        else:
            print("Incorrect command. Try again.")
            continue


def main():
    while True:
        number = random.randint(1,100)
        while True:
            result = choose_difficulty(number)
            if result == "win":
                print("Congratulation! You win!")
                break
            else:
                print("You lose.")
                break
        next_game = input("If you want to play again type 'yes' or press enter to quit game: ").lower().strip()
        if next_game == "yes":
            continue
        else:
            print("Goodbye!")
            break
        
main()