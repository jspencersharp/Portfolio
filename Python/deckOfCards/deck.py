from random import shuffle
import copy

class Deck(object):

    def  __init__(self):
        self.cardList = ["SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10" ,"SJ", "SQ", "SK", "HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10" ,"HJ", "HQ", "HK", "DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10" ,"DJ", "DQ", "DK", "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10" ,"CJ", "CQ", "CK"]
        self.availCards = []

    def shuffle(self):
        self.availCards = copy.deepcopy(self.cardList)
        shuffle(self.availCards)
        return self

    def draw(self):
        return self.availCards.pop()

    def count(self):
        return len(self.availCards)

myHand1 = []
myHand2 = []
myDeck = Deck()
myDeck.shuffle()

for count in range(0,5):
    myHand1.append(myDeck.draw())
    myHand2.append(myDeck.draw())

# print myDeck.count()

player1 = raw_input("Enter the name of the first player: ")
print player1, "has these cards -", myHand1

player2 = raw_input("Enter the name of the second player: ")
print player2, "has these cards -", myHand2