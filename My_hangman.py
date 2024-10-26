import random

def welcome_message():
    message = ("Welcome to the Hangman game. The computer will randomly choose a word, and your task is to guess it. \n"
               "Each time you guess an incorrect letter, a new part of the hangman drawing will appear. \n"
               "If you don’t guess the word in time, the man will be hanged.\n")
    return message

def hangman():
    HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   -+-
     | 
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | 
     |   | 
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | |
     |   | |
     |  
    ----------
    """)
    return HANGMAN
def choice_word():
    words = ["python","fish", "water", "gun", "flower"]
    word = random.choice(words)
    return word

def basic_information():
    word = choice_word()
    max_wrong = len(word) -1
    hidden_word = '-' * len(word)
    answer_player = ''
    return max_wrong, hidden_word, answer_player

def play_game():
    Hangman = hangman()
    word = choice_word()
    max_wrong, hidden_word, answer_player = basic_information()
    wrong = 0
    print(f"This is the word I chose {hidden_word}. Try to guess it, letter by letter\n")
    while wrong < max_wrong:
        guess_player = input("Enter a letter, and I’ll check if your letter is in my word: \n").lower().strip()
        if len(guess_player) != 1 or not guess_player.isalpha():
            print("Enter a letter.")
            continue
        if guess_player in hidden_word:
            print("This letter has already been guessed; try another one.")
            continue
        if guess_player in word:
            for i in range(len(word)):
                if guess_player == word[i]:
                    hidden_word = hidden_word[:i] + guess_player + hidden_word[i+1:]
                    print(f"The letter \'{guess_player}\' is in my word. The word now looks like this: {hidden_word} ")
            if hidden_word == word:
                print(f"Congratulation! You guessed! My word is: {word} ")
                break
        else:
            print(f"I'm sorry,that letter \"{guess_player}\" is not in my word.")
            print(Hangman[wrong])
            wrong += 1
            print(f"The word now looks like this: {hidden_word}")



    print(f"You've been hanged!. My word is: {word}")

def main():
    print(welcome_message())
    play_game()

if __name__ == "__main__":
    main()