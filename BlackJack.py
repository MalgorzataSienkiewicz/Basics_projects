import random

print("Welcome in game BLACK JACK.\n")
print("""Blackjack, also known as '21', is a popular card game where players compete against the dealer rather than each other.
The objective is to have a hand total closer to 21 than the dealer's hand, without exceeding 21.\n
Card values:
Number cards (2–10): Face value.
Face cards (Jack, Queen, King): 10 points.
Ace: 1 or 11 points, depending on which is more advantageous.\n 
Each player is dealt two cards one face-up and one face_down.\n
Players take turns deciding how to play their hand. Common actions:
Hit: Request another card to add to your total.
Stand: Keep your current total and end your turn.
Double Down: Receive one more card and end your turn.
Surrender (optional in some games): Forfeit half your bet to end your turn early.\n
The dealer reveals their face-down card and must play according to specific rules:
The dealer must hit if their hand totals 16 or less.
The dealer must stand on 17 or higher.\n
A hand totaling 21 with the first two cards (an Ace and a 10-value card) is called a Blackjack and win.
If your total exceeds 21, you "bust," and you lose the round, regardless of the dealer's hand.
If neither player nor dealer busts, the hand closest to 21 wins.
If the player and dealer have the same total, it’s a draw.\n
Let's start!   
      
""")

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
         "J" : 10
         }

player = []
croupier = []
player_cards = []
croupier_cards = []

def showing_cards(round):
    """Function to show the initial and final cards."""
    if round == 1 and len(player) != 0 and len(croupier) !=0: 
        print(f"One of the player's cards is: {player[0]}")
        print(f"One of the dealer's cards is: {croupier[0]}")
    else:
        print(f"Player cards: {player}")
        print(f"Dealer cards: {croupier_cards}")

def draw(draw_for='player'):
    """Function to draw a card for either player or croupier."""
    card = random.choice(list(cards.items())) 
    key, value = card
    if draw_for == "player":
            if key == "A":
                if sum(player) + value[1] <= 21:
                    player.append(value[1])
                    player_cards.append(key)
                else:
                    player.append(value[0])
                    player_cards.append(key)
            else:
                player.append(value)
                player_cards.append(key)
    else:
        if key == "A":
            if sum(croupier) + value[1] <= 21:
                croupier.append(value[1])
                croupier_cards.append(key)
            else:
                croupier.append(value[0])
                croupier_cards.append(key)
        else:
            croupier.append(value)
            croupier_cards.append(key)

def computer_move():
    """Function for the dealer's move."""
    while sum([i for i in croupier if isinstance(i,int)]) < 17:
        draw(draw_for='croupier')

    
def checking():
    """Function to check the results."""
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
    """Function for the hit option."""
    draw(draw_for='player')
    
        
def stand():
    """Function for the stand option."""
    computer_move()
    checking()


def double_down():
    """Function for the double down option."""
    hit()
    stand()


def choice_option():
    """Function for player to choose an option."""
    while True:
        print(f"Your cards: {player}")
        option = input("You have 4 options: hit, stand, double_down, surrender. What do you choose: ").lower().strip()
        if option == "hit":
            hit()
            if sum(player) > 21: 
                print("Player bust! Dealer wins.") 
                showing_cards(0)
                break
            if sum(croupier) == 21:
                print("Dealer wins!")
                print(f"Player cards: {player_cards}")
                print(f"Dealer cards: {croupier_cards}")
                break
            if sum(player) == 21:
                print("Player wins!")
                print(f"Player cards: {player_cards}")
                print(f"Dealer cards: {croupier_cards}")
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
    """Main function to start the game."""
    while True:
        global player, croupier, player_cards, croupier_cards
        player, croupier, player_cards, croupier_cards = [], [], [], []
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
        
        next_game = input("Are we playing again? Type 'yes' or press Enter and quit the game. ").lower().strip()
        if next_game == "yes":
            continue
        else:
            print("Goodbye!")
            break

            
main()
    



    



        