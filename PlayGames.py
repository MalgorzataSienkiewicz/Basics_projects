import BlackJack
import Number_Guessing_Game

if __name__ == "__main__":     
    
    print("Which game do you want to play?")
    print("1. BlackJack")
    print("2. Numer Guessing Game")
    game = input("Type correct number: ").lower().strip()
    
    if game == "1":
        BlackJack.blackJackInit()
    if game == "2":
        Number_Guessing_Game.numberGuessGameInit()
    else:
        print("Goodbye!")
