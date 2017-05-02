import random


class Deck:
    def __init__(self, shuffle, deal):
        self.shuffle = shuffle
        self.deal = deal

    def create_card(self):
        nm_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                     'K': 10}
        suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']
        [random.choice(val) for val in nm_values]:
            Deck(nm_values.items())

create_card()

#blackjack needs a dealer, player, cards, a deck, the ability to shuffle and deal, and the ability to check whether to hit
#for players, you can hit whenever...? Dealer gets a hit if their hand is below 17. Shuffle and deal belong to deck.
#Hand is its own class. 2 players and dealer will have hands to play.
#Deck is made up of cards. Cards have a suit, value, and rank.
#






#    def shuffle_deck(self, shuffle):






#create_card(self)






"""class Hand:
    def __init__(self):

class Dealer

list_comp = [num*n for num in input_list if num != 0]:
        new_list.append(list_comp)
"""

