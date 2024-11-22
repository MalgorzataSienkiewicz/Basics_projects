from random import randint

def checking(guess, number):
    if guess > number:
        return "To high."
    elif guess < number:
        return "To low."
    else:
        return "win"

def play_level(number, attempts):
    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except:
            print("You must type integer.")
            if attempts > 1:
                print(f"Try again")
            attempts -= 1
            continue
        else:
           result = checking(guess, number)
           if result != "win":
                if attempts > 1:
                    print(f"{result}. Guess again")
                attempts -= 1
           else:
               return "win"
    return "lose"

def choose_difficulty(number):
    while True:
        difficulty = input("Type 'easy' or 'hard': ").lower().strip()
        if difficulty == "easy":
             return play_level(number, 10)
        elif difficulty == "hard":
            return play_level(number, 5)
        else:
            print("Incorrect command. Try again.")
    
def numberGuessGameInit():
    while True:
        number = randint(1,100)
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
            
if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    numberGuessGameInit()