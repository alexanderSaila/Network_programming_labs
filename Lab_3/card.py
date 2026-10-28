class Card:
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    values = [
            "Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King"
            ]

    def __init__(self, suit, value):
        assert 1 <= suit <= 4 and 1 <= value <= 13
        self._suit = suit
        self._value = value


    def getValue(self):
        return self._value


    def getSuit(self):
        return self._suit


    def __str__(self):
        return f"{self.values[self._value-1]} of {self.suits[self._suit-1]}"