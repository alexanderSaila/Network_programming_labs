from card import Card
from card_deck import CardDeck

deck = CardDeck()
deck.shuffle()
while deck.size()>0:
    card = deck.getCard()
    print("Card {} has value {}".format(card, card.getValue()))