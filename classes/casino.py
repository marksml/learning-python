import random

class Die(object):

    def __init__(self,numberOfSides):
        self.numberOfSides = numberOfSides

    def roll(self):
        return random.randint(1,self.numberOfSides)

class Deck(object):

    def shuffle(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        ranks = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        
        # deck of cards that gets shauffled
        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(suit +" "+rank)

        random.shuffle(self.cards)  

    def deal(self):
        return self.cards.pop()



