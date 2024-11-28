import json
from random import choice

SCORE_TO_WIN = 5

with open("game_data.json", "r") as file:
    content = json.load(file)

def celebrity_draw():
    first_person = choice(content)
    second_person = choice(content)
    while first_person == second_person:
        second_person = choice(content)
    return first_person, second_person


def guessing(first_person, second_person):
    print(f"Compare 'A': {first_person['name']}, a {first_person['description']}, from {first_person['country']}.")
    print("VS")
    print(f"Compare 'B': {second_person['name']}, a {second_person['description']}, from {second_person['country']}.")
    while True:
        guess = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper().strip()
        if guess == "A" or guess == "B":
            return guess
        else:
            print("Incorrect command. Try again.")
            continue

'''@todo optimalize prints'''
def compare(first_person, second_person, guess, score):
        if guess == "A" and first_person["follower_count"] > second_person["follower_count"]:
            score += 1
            print(f"""You're right!
{first_person['name']} has {first_person['follower_count']} mln followers,
{second_person['name']} has {second_person['follower_count']} mln followers. 
Current score: {score}""")
        elif guess == "B" and second_person["follower_count"] > first_person["follower_count"]:
            score += 1
            print(f"""You're right! 
{first_person['name']} has {first_person['follower_count']} mln followers,
{second_person['name']} has {second_person['follower_count']} mln followers. 
Current score: {score}""")
        else:
            print(f"""Sorry, that's wrong.
{first_person['name']} has {first_person['follower_count']} mln followers,
{second_person['name']} has {second_person['follower_count']} mln followers.
Final score: {score}""")
            return False
        if score == SCORE_TO_WIN:
            print("Congratulation! You win!")
            return False
        return score

def game():
    while True:
        score = 0
        while True:
            first_person, second_person = celebrity_draw()
            guess = guessing(first_person, second_person)
            result = compare(first_person, second_person, guess, score)
            if result is False:
                break
            else:
                score = result

        if result is False:
            next_game = input("Do you want play again? Type 'yes' or press Enter and quit the game: ").lower().strip()
            if next_game != "yes":
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    print("Welcome in Higher Lower game!")
    print("If your answer is correct, I will give you 1 point. Otherwise, you lose immediately.")
    print("You win if your score is equal to 5.\n")
    game()












