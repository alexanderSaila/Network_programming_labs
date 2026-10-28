import random
from card import Card

class CardDeck:
    
    
    def __init__(self):
        self.reset()
        self.shuffle()
    
    
    def shuffle(self):
        shuffledDeck = []
        while len(self._deck) > 0:
            pick = random.randint(0, len(self._deck)-1)
            card = self._deck.pop(pick)
            shuffledDeck.append(card)
        
        self._deck = shuffledDeck
    
    
    def getCard(self):
        return self._deck.pop(len(self._deck)-1)
    
    
    def size(self):
        return len(self._deck)
    
    
    def reset(self):
        self._deck = []
        for suit in range(1,5):
            for value in range(1,14):
                self._deck.append(Card(suit, value))