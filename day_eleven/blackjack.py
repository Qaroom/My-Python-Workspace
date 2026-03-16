import random

blackjack_cards = {
    "A": [1, 11],
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}
player_cards=[]
dealer_cards=[]
get_blackjack_cards=dict.copy(blackjack_cards)

def get_cards(card_list,count=1):
    for _ in range(count):
        key=random.choice(list(get_blackjack_cards.keys()))
        card_list.append(key)
        get_blackjack_cards.pop(key)


def get_cards_values(cards):
    value = 0
    aces = 0
    for card in cards:
        if card == "A":
            aces += 1
            value += 11 
        else:
            value += blackjack_cards[card]

    while value > 21 and aces > 0:
        value -= 10  
        aces -= 1

    return value


def control_cards(operation_type):
    total_player=get_cards_values(player_cards)
    total_dealer=get_cards_values(dealer_cards)
    if total_player <= 21:
        if operation_type == "hit":
            get_cards(player_cards)
            total_player=get_cards_values(player_cards)
            if total_player  <= 21:
                print(f"Dealer :{blackjack_cards[dealer_cards[0]]}")
                return total_player,total_dealer ,True

            else : 
                print("Dealer win")
                print(f"Dealer :{total_dealer}")
                return total_player,total_dealer ,False
            
            
        else : 
            while True: 
                total_dealer=get_cards_values(dealer_cards)
                if total_dealer > total_player and total_dealer<=21:
                    print("Dealer win")
                    print(f"Dealer :{total_dealer}")
                    return total_player,total_dealer ,False
                elif total_dealer < total_player : 
                    get_cards(dealer_cards)
                elif total_dealer >21:
                    print("Player Win")
                    print(f"Dealer :{total_dealer}")
                    return total_player,total_dealer ,False
    else : 
        print("Dealer win")
        print(f"Dealer :{total_dealer}")
        return total_player,total_dealer ,False

def main():
    get_cards(player_cards,2)
    get_cards(dealer_cards,2)
    print(f"Player :{get_cards_values(player_cards)}")
    print(f"Dealer :{blackjack_cards[dealer_cards[0]]}")

    while True:
        operation_type=input("Type Hit Or Stand\n").lower()
        t_p,_,c_p= control_cards(operation_type)
        print(f"Player :{t_p}")
        if c_p == False:
            print(f"Player Cards :{player_cards}")
            print(f"Dealer Cards :{dealer_cards}")
            break

main()
