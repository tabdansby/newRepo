import random

class Deck:
    def __init__(self, shuffle, deal):
        self.shuffle = shuffle
        self.deal = deal

class Cards:
   def __init__(self, rank, value, suit):
       self.rank = rank
       self.value = value
       self.suit = suit

    def create_card(self):
        rank = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
        value = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
        suit = {'Diamonds', 'Spades', 'Hearts', 'Clubs'}

        pick = [random.choice(self.rank) for i in rank]

"""class Hand:
    def __init__(self):

class Dealer

list_comp = [num*n for num in input_list if num != 0]:
        new_list.append(list_comp)
"""

