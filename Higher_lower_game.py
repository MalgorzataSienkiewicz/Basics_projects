import json
from random import choice
print("Welcome in higher lower game!")
score = 0
with open("game_data.json", "r") as file:
    content = json.load(file)

def celebrity_draw():
    first_person = choice(content)
    second_person = choice(content)
    return first_person, second_person

def compare():
    first_person, second_person = celebrity_draw()
    print(f"Compare 'A': {first_person['name']}, a {first_person['description']}, from {first_person['country']}")
    print("VS")
    print(f"Compare 'B': {second_person['name']}, a {second_person['description']}, from {second_person['country']}")
    guess = input("Who has more followers on Instagram? Type 'A' or 'B'").upper().strip()








