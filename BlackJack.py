import random

print("Welcome in game BLACK JACK.")

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

def showing_cards():
    round == 1
    if round == 1:
        player_card = random.choice(player)  
        print(f"One of the player's cards is: {player_card}")
        croupier_card = random.choice(croupier)
        print(f"One of the dealer's cards is: {croupier_card}")
    else:
        print(f"Player cards: {player}")
        print(f"Dealer cards: {croupier}")
    return 


def draw(round):
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
        round = 0
    else:
        choice = random.choice(cards)
        if draw_player == 'yes':
            player.append(choice)
        else:
            croupier.append(choice)
    return key, value 

def computer_move():
    if sum(croupier) < 17 and sum(croupier) < 21:
        draw()


    
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
        print(f"Your cards: {player}")
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
    
def main():
    round = 1
    draw(round)
    showing_cards(round)
    while True:
        draw_player = "yes"
        if draw_player == "yes":
            if sum(player) > 21:
                print("You lose.")
                break
            else:
                choice_option()
                draw_player = "no"
                if sum(player) > 21:
                    print("You lose.")
                    break

        else:
            computer_move()
            draw_player = "yes"
            if sum(croupier) > 21:
                print("Computer lose.")
            
main()
    



    



        