import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1,100)

def checking(guess,number):
    if guess > number:
        return "To high."
    elif guess < number:
        return"To low."
    else:
        return "win"


def easy_level(number):
    attempts = 10
    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except:
            print("You must type integer. Try again")
            attempts -= 1
            continue
        else:
           result= checking(guess,number)
           if result != "win":
               print(f"{result}. Guess again")
               attempts -= 1
           else:
               return "win"
    return "lose"


def hard_level(number):
    attempts = 5
    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except:
            print("You must type integer. Try again")
            attempts -= 1
            continue
        else:
           result = checking(guess,number)
           print(f"{result}. Guess again.")
           if result != "win":
               attempts -= 1
           else:
               return "win"
    return "lose"
    

def choose_difficulty(number):
    while True:
        difficulty = input("Type 'easy' or 'hard': ").lower().strip()
        if difficulty == "easy":
             return easy_level(number)
        elif difficulty == "hard":
            return hard_level(number)
        else:
            print("Incorrect command. Try again.")

    
def main():
    while True:
        number = random.randint(1,100)
        result = choose_difficulty(number)
        if result == "win":
            print("Congratulation! You win!")   
        else:
            print(f"You lose. My number is: {number}")
            
        next_game = input("If you want to play again type 'yes' or press Enter to quit game: ").lower().strip()
        if next_game == "yes":
            continue
        else:
            print("Goodbye!")
            break
        
main()