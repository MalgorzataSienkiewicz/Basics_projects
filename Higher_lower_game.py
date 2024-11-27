import json
from random import choice
print("Welcome in higher lower game!")
with open("game_data.json", "r") as file:
    content = json.load(file)

def celebrity_draw():
    first_person = choice(content)
    second_person = choice(content)
    return first_person, second_person

def compare(first_person, second_person):
    print(f"Compare 'A': {first_person['name']}, a {first_person['description']}, from {first_person['country']}.")
    print("VS")
    print(f"Compare 'B': {second_person['name']}, a {second_person['description']}, from {second_person['country']}.")
    while True:
        guess = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper().strip()
        if guess == "A" or guess == "B":
            continue
        else:
            print("Incorrect command.")
    return guess

def game():
    score = 0
    while True:
        first_person, second_person = celebrity_draw()
        guess = compare(first_person,second_person)
        if guess == "A" and first_person["follower_count"] > second_person["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            continue
        elif guess == "B" and second_person["follower_count"] > first_person["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            continue
        else:
            print(f"Sorry, that's wrong. Final score: {score}" )
            next_game = input("Do you want play again? Type 'yes' or press Enter and quit the game.").lower().strip()
            if next_game == "yes":
                score = 0
                continue
            else:
                break
        break


game()












