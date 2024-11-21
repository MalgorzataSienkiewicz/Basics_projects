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
player_cards = []
croupier_cards = []

def showing_cards(round):
    if round == 1 and len(player) != 0 and len(croupier) !=0: 
        print(f"One of the player's cards is: {player[0]}")
        print(f"One of the dealer's cards is: {croupier[0]}")
    else:
        print(f"Player cards: {player}")

def draw(draw_for='player'):
    card = random.choice(list(cards.items())) 
    key, value = card
    if draw_for == "player":
            if key == "A":
                choice = int(input("Will your card count as 1 or 11? ")) 
                player.append(choice)
                player_cards.append(key)
            else:
                player.append(value)
                player_cards.append(key)
    else:
        if key == "A":
            if sum(croupier) <= 10:
                croupier.append(value[1])
            else:
                croupier.append(value[0])
        else:
            croupier.append(value)
            croupier_cards.append(key)

def computer_move():
    while sum([i for i in croupier if isinstance(i,int)]) < 17:
        draw(draw_for='croupier')

    
def checking():
    print(player)
    score_player = sum(player)
    score_croupier = sum(croupier)
    if score_player > 21:
        print("Player bust! Dealer wins.")
    elif score_croupier > 21:
        print("Dealer bust! Player wins.")
    elif score_croupier == 21:
        print("Dealer wins!")
    elif score_player == 21:
        print("Player wins!.")
    elif score_player > score_croupier:
        print("Players wins!")
    elif score_player < score_croupier:
        print("Dealer wins!")
    else:
        print("It's a draw!")
    print(f"Player cards: {player_cards}")
    print(f"Dealer cards: {croupier_cards}")
    

def hit():
    draw(draw_for='player')


def stand():
    computer_move()
    checking()


def double_down():
    hit()
    stand()


def choice_option():
    while True:
        print(f"Your cards: {player}")
        option = input("You have 5 options: hit, stand, double_down, surrender. What do you choose: ").lower().strip()
        if option == "hit":
            hit()
            if sum(player) > 21: 
                print("Player bust! Dealer wins.") 
                showing_cards(0)
                break
            continue
        elif option == "stand":
            stand()
            break
        elif option == "double_down":
            double_down()
            break
        elif option == "surrender":
            print("Player surrenders. Dealer wins.")
            break
        else:
            print("Incorrect command. Try again.")
            continue
    return False

    
def main():
    round = 1
    if round == 1:
        for _ in range(2):
            draw(draw_for= 'player')
            draw(draw_for='croupier')
        showing_cards(round)
        round = 2
    else:
        showing_cards(round)

    while sum(player) <= 21 and choice_option():
        pass
            
main()
    



    



        