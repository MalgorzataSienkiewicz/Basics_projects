import random

cards = {"A" : [1,11],
         "2" : 2,
         "3" : 3,
         "4" : 4,
         "5" : 5,
         "6" : 6,
         "7" : 7,
         "8" : 8,
         "9" : 9,
         "10" : 10,
         "K" : 10,
         "Q" : 10,
         "W" : 10
         }
player = []
croupier = []

def draw():
    round = 1
    draw_player = "yes"

    if round == 1:
        for i in range(2):
            choice = random.choice(cards)
            for key, value in choice.items():
                if range == 0:
                    player.append(value)
                else:
                    croupier.append(value)
    else:
        choice = random.choice(cards)
        if draw_player == 'yes':
            player.append(choice)
        else:
            croupier.append(choice)

def checking():
    score_player = sum(player)
    score_croupier = sum(croupier)
    winner = ''
    if score_player > score_croupier:
        winner = "Player win."
    elif score_player == score_croupier:
        winner = "It's a draw."
    else:
        winner = "Croupier win."
    return winner
    

def hit():
    draw()
    

def stand():
    checking()

def double_down():
    draw()
    checking()

def split():
    pass

def surrender():
    print("You lose.")

def choice_option():
    while True:
        option = input("You have 5 options: hit, stand, double_down, split, surrender. What do you choose: ")
        if option == "hit":
            hit()
        elif option == "stand":
            stand()
        elif option == "double_down":
            double_down()
        elif option == "split":
            split()
        elif option == "surrender":
            surrender()
        else:
            print("Incorrect command. Try again.")
            continue
    

    



        