import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    if input("Do you want to play a game of Blackjack?\n Type 'y' or 'n': ") == 'n':
        play_blackjack = False
    else:
        play_blackjack = True

    while play_blackjack:
        print(logo)
        c1 = random.choice(cards)
        c2 = random.choice(cards)

        score = c1 + c2
        start_hand = [c1, c2]
        computer_choice = random.choice(cards)

        print(f"Your cards are {start_hand}, current score: {score}")
        print(f"Computer's first card: {computer_choice}")

        if input("Type 'y' to get another card, type 'n' to pass") == 'y':
            add_card = True
        else:
            add_card = False

        while add_card:
            new_card = random.choice(cards)
            score = score + new_card
            hand = start_hand
            hand.append(new_card)
            print(f"Your cards are {hand}, current score is {score}")
            if input("Type 'y' to get another card, type 'n' to pass") == 'y':
                add_card = True
            else:
                add_card = False
        blackjack()


blackjack()
